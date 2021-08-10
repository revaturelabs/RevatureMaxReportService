# create table associate(
#     salesforceId varchar(10) primary key not null,
#     firstname varchar(20) not null,
#     lastname varchar(20) not null,
#     email varchar(40) UNIQUE,
#     pswrd varchar(40)
# );
from src.model.associate import Associate
associates = [
    Associate("ex0001@example.com", "EX-0001", "ExFirst1", "ExLast1", "EX-B01"),
    Associate("ex0002@example.com", "EX-0002", "ExFirst2", "ExLast2", "EX-B01"),
    Associate("ex0003@example.com", "EX-0003", "ExFirst3", "ExLast3", "EX-B01"),
    Associate("ex0004@example.com", "EX-0004", "ExFirst4", "ExLast4", "EX-B01"),
    Associate("ex0005@example.com", "EX-0005", "ExFirst5", "ExLast5", "EX-B02"),
    Associate("ex0006@example.com", "EX-0006", "ExFirst6", "ExLast6", "EX-B02"),
    Associate("ex0007@example.com", "EX-0007", "ExFirst7", "ExLast7", "EX-B02"),
    Associate("ex0008@example.com", "EX-0008", "ExFirst8", "ExLast8", "EX-B02"),
    Associate("ex0009@example.com", "EX-0009", "ExFirst9", "ExLast9", "EX-B02"),
]
