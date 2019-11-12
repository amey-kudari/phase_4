drop database if exists GNU;
create database GNU;
use GNU;

drop table if exists STAFF;
drop table if exists PATIENT;
drop table if exists WING;
drop table if exists ROOM;
drop table if exists DEPENDENT;
drop table if exists DOCTORS;
drop table if exists DOCTOR;
drop table if exists NURSE;
drop table if exists NURSES;
drop table if exists WORKS_WITH;
drop table if exists SPECIALITY;
drop table if exists QUALIFICATIONS;
drop table if exists TREATS;
drop table if exists TREATED;

create table STAFF(
	StaffID INT,
	Fname	VARCHAR(50),
	Minit	VARCHAR(3),
	Lname	VARCHAR(50),
	DOB		DATE,
	DOJ		DATE,
	Wdays	INT,
	Salary_hr	INT,
	Whours	INT
	);

create table PATIENT(
	PatientID	INT,
	Fname		VARCHAR(50),
	Minit		VARCHAR(3),
	Lname		VARCHAR(50),
	DOB			DATE,
	WingID		INT
	);

create table WING(
	WingID 		INT,
	Warden		INT
	);

create table ROOM(
	WingID		INT,
	RoomNo		INT,
	Floor		INT,
	Cost		INT
	);

create table DEPENDENT(
	StaffID		INT,
	Fname		VARCHAR(50),
	Minit		VARCHAR(3),
	Lname		VARCHAR(50),
	Sex			VARCHAR(50),
	DOB			DATE,
	Relationship VARCHAR(50)
	);

create table DOCTOR(
	PatientID	INT,
	DoctorID	INT
	);

create table DOCTORS(
	StaffID 	INT,
	SuperID		INT,
	OfficeNo	INT,
	OnCall		VARCHAR(3)
	);

create table NURSE(
	StaffID		INT,
	DoctorID	INT,
	PatientID	INT
	);

create table NURSES(
	PatientID	INT,
	NurseID		INT
	);

create table WORKS_WITH(
	DoctorID 	INT,
	NurseID		INT
	);

create table TREATS(
	DoctorID	INT,
	PatientID	INT
	);

create table TREATED(
	PatientID	INT,
	WingID		INT,
	NurseID		INT,
	DoctorID	INT
	);

create table SPECIALITY(
	DoctorID 	INT,
	Spec   		VARCHAR(50)
	);

create table QUALIFICATIONS(
	DoctorID 	INT,
	Qual   		VARCHAR(50)
	);


