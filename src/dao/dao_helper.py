from config.db_config import get_connection
from config.loggingConfig import controller_log as logger


def cursor_handler(decorated):
    """Injects a database cursor into the function parameters
    note that the original function is still callable
    without supplying the `cursor`"""
    def f(*args, **kwargs):
        logger.name = decorated.__module__
        conn = None
        result = None
        try:
            conn = get_connection()
            if not conn:
                logger.exception(f"{decorated.__name__} :: connection failed to initialize.")
                return None
            with conn.cursor() as cur:
                if not cur:
                    logger.exception(f"{decorated.__name__} :: cursor failed to initialize.")
                    return None
                result = decorated(*args, **kwargs, cursor=cur)
                cur.close()
            conn.commit()
        except Exception as e:
            logger.exception(f'{decorated.__name__} :: Unhandled exception: {e}')
        finally:
            if conn:
                conn.close()
            return result
    f.__name__ = decorated.__name__
    return f
