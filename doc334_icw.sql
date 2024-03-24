-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2022 at 02:32 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `doc334_icw`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `BookNo` varchar(6) NOT NULL,
  `Title` varchar(220) DEFAULT NULL,
  `SubjectCode` varchar(3) DEFAULT NULL,
  `Author` varchar(50) DEFAULT NULL,
  `Publisher` varchar(50) DEFAULT NULL,
  `YearPublished` int(4) DEFAULT NULL,
  `Price` int(5) DEFAULT NULL,
  `ISBN` varchar(14) DEFAULT NULL,
  `Location` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`BookNo`, `Title`, `SubjectCode`, `Author`, `Publisher`, `YearPublished`, `Price`, `ISBN`, `Location`) VALUES
('B00001', 'Sherlock Holmes The Hound Of The Baskervilles\r\n', 'S00', 'Sir Author Conan Doyle\r\n', 'Spero Independant Publishing Group\r\n', 1914, 1200, '9789557169057\r', 'A01'),
('B00002', 'Alex Rider Mission 7:Snakehead', 'S01', 'Anthony Horowitz', 'Walker Books', 2012, 1500, '9781406310399', 'B01');

-- --------------------------------------------------------

--
-- Table structure for table `chapter`
--

CREATE TABLE `chapter` (
  `BookNo` varchar(6) DEFAULT NULL,
  `ChapterNo` int(4) DEFAULT NULL,
  `ChapterTitle` varchar(250) DEFAULT NULL,
  `StartPage` int(5) DEFAULT NULL,
  `EndPage` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chapter`
--

INSERT INTO `chapter` (`BookNo`, `ChapterNo`, `ChapterTitle`, `StartPage`, `EndPage`) VALUES
('B00001', 1, 'Mr Sherlock Holmes', 3, 6),
('B00001', 2, 'The Curse of the Baskervilles', 10, 31),
('B00001', 3, 'The Problem', 32, 43),
('B00001', 4, 'Sir Henry Baskerville', 44, 53),
('B00001', 5, 'Three Broken Threads', 54, 63),
('B00001', 6, 'Baskerville Hall', 64, 77),
('B00001', 7, 'The Stapletone of the Merripit House', 78, 84),
('B00001', 8, 'First Report of Dr Watson', 85, 101),
('B00001', 9, 'The Light upon the Moor', 102, 111),
('B00001', 10, 'Extract from the Diary of Dr Watson', 112, 124),
('B00001', 11, 'The Man on the Tor', 125, 136),
('B00001', 12, 'Death on the Moor', 137, 148),
('B00001', 13, 'Fixing the Nets', 149, 160),
('B00001', 14, 'The Hounds of the Baskervilles', 161, 172),
('B00001', 15, 'A Retrospection', 173, 181);

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `SubjectCode` varchar(3) NOT NULL,
  `SubjectName` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`SubjectCode`, `SubjectName`) VALUES
('S00', 'Mystery'),
('S01', 'Adventure');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`BookNo`),
  ADD KEY `SubjectCode` (`SubjectCode`);

--
-- Indexes for table `chapter`
--
ALTER TABLE `chapter`
  ADD KEY `BookNo` (`BookNo`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`SubjectCode`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `book_ibfk_1` FOREIGN KEY (`SubjectCode`) REFERENCES `subject` (`SubjectCode`);

--
-- Constraints for table `chapter`
--
ALTER TABLE `chapter`
  ADD CONSTRAINT `chapter_ibfk_1` FOREIGN KEY (`BookNo`) REFERENCES `book` (`BookNo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
