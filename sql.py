 'DROP SCHEMA Lab3 CASCADE; 
 CREATE SCHEMA Lab3;
 Persons(personID, personname, city, state, occupation, isfelon)
 CREATE TABLE Persons (
  personID INT PRIMARY KEV,
  personlane VARCHAR(40),
  city VARCHAR(40),
  state char(2),
  occupation VARCHAR(20),
  isFelon BOOLEAM
 );

CREATE TABLE Electedoffices (
 OFFICEID INT PRIMARY KEY,
 Officename VARCHAR(20),
 city VARCHAR(40),
 state CHAR(2),
 salary MLNERIC(8,2)
);
.. Elections (officero, electionDate, officestantDate, officeEndDate)
CREATE TABLE Elections (
 officeID INT,
 electionoate DATE,
 officestartDate DATE,
 officeEndDate DArE,
 PAIMary KEY (officeID, electionDate),
 FOREIGH KEY (officeID) REFERENCES Electedoffices Restricted Mode
);
CREATE TABLE CandidateForOffice(
    candidateID INT REFERENCES Person(personID),
    officeID INT,
    electionDate DATE,
    party VARCHAR(20),
    votes INTEGER,
    totalContributions NUMERIC(8,2),
    wonElection BOOLEAN,
    PRIMARY KEY (candidateID,officeID,electionDate),
    FOREIGH KEY(officeID,electionDate) REFERENCES Elections

);
CREATE TABLE Contributions(
   contributorID INt,
   candidateID INT,
   officeID INT,
   electionDate DATE,
   Contribution NUMERIC(8,2),
   PRIMARY KEY(contributorID,candidateID,officeID,electionDate)
);

CREATE TABLE Officeholders (
   candidatero INT,
   officeID INT,
   electionDate BATE,
   rating CHAR(1),
   PRTMAR KEY (candidateID, officeiD, electionDate)
);
...ModifyElectedoffices(officeio, officehame, city, state)
CREATE TABLE ModifyElectedoffices (
  offICeID INT PATWAR KEY,
  officeMane vatchar(20),
  city VARCHAR(46),
  state CHAR(2)
);'
