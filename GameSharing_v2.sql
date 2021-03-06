DROP TABLE IF EXISTS
	Client, Orders, ClientOrders, GameStat, Storage, Game, Event, ClientGame
	CASCADE
;
CREATE TABLE Client (
Id VARCHAR(20) NOT NULL PRIMARY KEY,
FullName VARCHAR(20) NOT NULL,
PhoneNum VARCHAR(20) NOT NULL,
Email VARCHAR(20) NOT NULL,
Password VARCHAR(20) NOT NULL
);
CREATE TABLE Orders(
Id VARCHAR(20) NOT NULL PRIMARY KEY,
ClientId VARCHAR(20) NOT NULL references Client(Id),
RentCost INT NOT NULL,
CollateralAmount INT NOT NULL,
Status INT NOT NULL,
BookTime TIME NOT NULL,
LastGameTime TIME NOT NULL,
BookCost INT NOT NULL
);

CREATE TABLE GameStat (
Id VARCHAR(20) NOT NULL PRIMARY KEY,
Name VARCHAR(20) NOT NULL,
Amount INT NOT NULL,
Type BOOL NOT NULL,
GameTime TIME NOT NULL,
BoxPrice INT NOT NULL,
RequestCount INT NOT NULL,
RentCost INT NOT NULL,
FreeBoxCount INT NOT NULL,
Image VARCHAR(20) NOT NULL,
Description VARCHAR(200) NOT NULL
);

CREATE TABLE Storage (
Address VARCHAR(20) NOT NULL PRIMARY KEY,
FreeCellCount INT NOT NULL,
RentCost INT NOT NULL,
UsageCount INT NOT NULL
);

CREATE TABLE Game (
BoxId VARCHAR(20) NOT NULL PRIMARY KEY,
StatId VARCHAR(20) references GameStat(Id),
StorageAddress VARCHAR(20) references Storage(Address),
Free BOOL NOT NULL,
Sold BOOL NOT NULL,
AccessCode INT NOT NULL,
ReturnTime TIME NOT NULL,
LastOrderId VARCHAR(20) NOT NULL
);

CREATE TABLE Event(
Id VARCHAR(20) NOT NULL PRIMARY KEY,
OrderId VARCHAR(20) NOT NULL references Orders(Id),
BoxId VARCHAR(20) NOT NULL references Game(BoxId),
Type INT NOT NULL
);

CREATE TABLE ClientGame(
ClientGameId VARCHAR(20) NOT NULL PRIMARY KEY,
StatId VARCHAR(20) NOT NULL references GameStat(Id),
ClientId VARCHAR(20) NOT NULL references Client(Id),
ReceptionDate DATE NOT NULL
);

