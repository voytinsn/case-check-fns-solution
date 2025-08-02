-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Хост: mysql
-- Время создания: Июл 30 2025 г., 15:39
-- Версия сервера: 9.4.0
-- Версия PHP: 8.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `crm`
--

-- --------------------------------------------------------

--
-- Структура таблицы `clients`
--

CREATE TABLE `clients` (
  `id` int NOT NULL,
  `company_name` text COLLATE utf8mb4_general_ci NOT NULL,
  `adress` text COLLATE utf8mb4_general_ci,
  `inn` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `okved` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `director` text COLLATE utf8mb4_general_ci,
  `director_function` text COLLATE utf8mb4_general_ci,
  `date_reg` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `clients`
--

INSERT INTO clients (id, company_name, adress, inn, okved, director, director_function, date_reg) VALUES
(1, 'Спецмед', NULL, '2312205769', NULL, NULL, 'Директор', NULL),
(2, 'ООО "СПЕЦАВТОХОЗЯЙСТВО"', 'обл. Иркутская, г. Иркутск, ул. Седова, д.30, пом.4', '3811133818', '38.1', NULL, NULL, '2009-10-22'),
(3, 'СПК "Заря"', NULL, '916005310', '01.41', 'Хасанов Борис Магометович', NULL, '2008-02-08'),
(4, 'ООО СК "СтройСервис"', NULL, '6950035740', '41.20', 'Чабров Игорь', NULL, NULL),
(5, 'Медцентр Доктор Плюс', 'обл. Самарская, г. Сызрань, пр-кт 50 Лет Октября, д.30, оф.1,2', '6325046418', '86.23', 'Шлёнский Денис Евгеньевич', 'Директор', NULL),
(6, 'ФЭШН ДИЗ ГРУП', NULL, '7719884986', '46.42', 'Рябчук Глеб Сергеевич', 'Генеральный директор', NULL),
(7, 'ООО "ЯЛТИНСКАЯ МЕТАЛЛОБАЗА"', 'обл. Ростовская, р-н Аксайский, г. Аксай, ул. Шолохова, зд.1', '9103007325', '46.72', NULL, NULL, '2014-10-21'),
(8, 'ООО "КВАЗАР"', NULL, '4909131590', '07.29.41', 'Дьячков Игорь Геннадьевич', 'Директор', NULL),
(9, 'ДЕЛОВАЯ РУСЬ', NULL, '6829102630', '79.11', NULL, 'Генеральный директор', NULL),
(10, 'ООО "МАСТЕР СЛОВА"', 'обл. Иркутская, г. Иркутск, ул. Декабрьских Событий, д.103, оф.19', '3849014369', '96.09', 'Пожарский Дмитрий Петрович', NULL, NULL);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `clients`
--
ALTER TABLE `clients`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
