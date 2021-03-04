DROP TABLE IF EXISTS
	Client, Orders, ClientOrders, GameStat, Storage, Cell, CellsInStorage, Game, StatInGame, Rent, Return
	CASCADE
;
CREATE TABLE Client (
Id VARCHAR(20) NOT NULL PRIMARY KEY,
FullName VARCHAR(20) NOT NULL,
PhoneNum VARCHAR(20) NOT NULL
);
CREATE TABLE Orders(
Id VARCHAR(20) NOT NULL PRIMARY KEY,
ClientId VARCHAR(20) NOT NULL references Client(Id),
RentCost INT NOT NULL,
PledgeAmount INT NOT NULL,
Status INT NOT NULL
);

CREATE TABLE ClientOrders(
ClientId VARCHAR(20) NOT NULL references Client(Id),
OrderId VARCHAR(20) NOT NULL references Orders(Id),
PRIMARY KEY (ClientId, OrderId)
);

CREATE TABLE GameStat (
Barcode VARCHAR(20) NOT NULL PRIMARY KEY,
Name VARCHAR(20) NOT NULL,
Amount INT NOT NULL,
Type BOOL NOT NULL,
GameTime TIME NOT NULL,
BoxPrice INT NOT NULL,
RequestCount INT NOT NULL,
RentCost INT NOT NULL
);

CREATE TABLE Storage (
Address VARCHAR(20) NOT NULL PRIMARY KEY,
FreeCell INT NOT NULL,
RentCost INT NOT NULL
);

CREATE TABLE Cell (
Id VARCHAR(20) NOT NULL,
Free BOOL NOT NULL,
PRIMARY KEY(Id)
);
CREATE TABLE CellsInStorage(
Storage VARCHAR(20) NOT NULL references Storage(Address),
Cell VARCHAR(20) NOT NULL references Cell(Id)
);
CREATE TABLE Game (
BoxId VARCHAR(20) NOT NULL PRIMARY KEY,
CellId VARCHAR(20) references Cell(Id),
Free BOOL NOT NULL,
OrderCount INT NOT NULL,
Sold BOOL NOT NULL
);

CREATE TABLE StatInGame (
Statistic VARCHAR(20) NOT NULL references GameStat(Barcode),
Game VARCHAR(20) NOT NULL references Game(BoxId),
PRIMARY KEY(Statistic, Game)
);

CREATE TABLE Rent (
Id VARCHAR(20) NOT NULL PRIMARY KEY,
OrderId VARCHAR(20) NOT NULL references Orders(Id),
CellId VARCHAR(20) NOT NULL references Cell(Id),
Time TIME NOT NULL,
BoxId VARCHAR(20) NOT NULL references Game(BoxId)
);

CREATE TABLE Return (
Id VARCHAR(20) NOT NULL PRIMARY KEY,
OrderId VARCHAR(20) NOT NULL references Orders(Id),
CellId VARCHAR(20) references Cell(Id),
Time TIME NOT NULL,
BoxId VARCHAR(20) NOT NULL references Game(BoxId)
);

