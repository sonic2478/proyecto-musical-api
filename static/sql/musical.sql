-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-11-2023 a las 17:54:19
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `musical`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cancion`
--

CREATE TABLE `cancion` (
  `idcancion` int(11) NOT NULL,
  `nombrec` varchar(105) NOT NULL,
  `artistac` varchar(105) NOT NULL,
  `albumc` varchar(105) NOT NULL,
  `fechac` year(4) NOT NULL,
  `generoc` varchar(105) NOT NULL,
  `nombreimg` varchar(105) NOT NULL,
  `fechareg` datetime NOT NULL,
  `urlc` varchar(2050) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cancion`
--

INSERT INTO `cancion` (`idcancion`, `nombrec`, `artistac`, `albumc`, `fechac`, `generoc`, `nombreimg`, `fechareg`, `urlc`) VALUES
(1, 'Every Breath You Take', 'The Police', 'Synchronicity', 1983, 'Soft rock', 'everybreath.jpg', '2023-10-03 10:02:00', 'https://open.spotify.com/intl-es/track/1JSTJqkT5qHq8MDJnJbRE1'),
(2, 'Enchanted (Taylor\'s Version)', 'Taylor Swift', 'Speak Now (Taylor\'s Version)', 2023, 'Pop rock', 'enchanted.jpg', '2023-10-03 10:09:00', 'https://open.spotify.com/intl-es/track/3sW3oSbzsfecv9XoUdGs7h'),
(3, 'Heavenly', 'Cigarettes After Sex', 'Cry', 2019, 'Alternativa ', 'heavenly.jpg', '2023-10-03 10:11:00', 'https://open.spotify.com/intl-es/track/70YTBH8vOGJNMhy6186yFm'),
(4, 'Demons', 'Imagine Dragons', 'Night Visions', 2012, 'Rock alternativo', 'demons.jpg', '2023-10-03 10:13:00', 'https://open.spotify.com/intl-es/track/3LlAyCYU26dvFZBDUIMb7a'),
(5, 'Sunflower', 'Post Malone, Swae Lee', ' Spider?Man: Into the Spider?Verse (Soundtrack From & Inspired by the Motion Picture)', 2018, 'Hip hop', 'sunflower.jpg', '2023-10-03 10:15:00', 'https://open.spotify.com/intl-es/track/3KkXRkHbMCARz0aVfEt68P'),
(6, 'Hummingbird', 'Metro Boomin, James Blake', ' METRO BOOMIN PRESENTS SPIDER?MAN: ACROSS THE SPIDER?VERSE: SOUNDTRACK FROM AND INSPIRED BY THE MOTION PI', 2023, 'Urbano latino', 'hummingbird.jpg', '2023-10-03 10:18:00', 'https://open.spotify.com/intl-es/track/6HexNTb392JS071DoTGo0y'),
(7, 'Mi suerte', 'Morat', 'Balas perdidas', 2018, 'Balada', 'misuerte.jpg', '2023-10-03 10:21:00', 'https://open.spotify.com/intl-es/track/2kVtMvrlcK5SRxZvdHgTzn'),
(8, 'Heart Made Up On You', 'R5', 'Sometime Last Night', 2015, 'Pop', 'heartmade.jpg', '2023-10-03 10:24:00', 'https://open.spotify.com/intl-es/track/3fuh7odDvD0bGEO9HIF8MQ'),
(9, 'Enjoy The Silence', 'Depeche Mode', 'Violator', 1990, 'Synth pop', 'enjoysilence.jpg', '2023-10-03 10:26:00', 'https://open.spotify.com/intl-es/track/1EjQRTG53jsinzk2xlVVJP'),
(12, 'Afuera', 'Caifanes', 'El nervio del volcán', 1994, 'Rock', 'afuera.jpg', '2023-10-03 10:28:00', 'https://open.spotify.com/intl-es/track/3pJfnBjO3kjudEchcPEDxS');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inserta`
--

CREATE TABLE `inserta` (
  `idinserta` int(11) NOT NULL,
  `idcancion` int(11) NOT NULL,
  `fechai` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombreu` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `correou` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `claveu` varchar(105) COLLATE utf8_spanish_ci NOT NULL,
  `perfilu` char(1) COLLATE utf8_spanish_ci NOT NULL DEFAULT 'S'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombreu`, `correou`, `claveu`, `perfilu`) VALUES
(2, 'sam', 'sam@gmail.com', 'pbkdf2:sha256:600000$Z00Sxwrb0nWYxbWx$96708d2834f98a9cdb1b0862ef075744227478d46a97f05ee8e4e1b6ec4d4820', 'A'),
(4, 'holaaaaa', 'cas@gmail.com', 'pbkdf2:sha256:600000$5x2sb9u26jmO4Hx3$4fed917926ccea1a1f69b2967b64e401a77b4da57c0edd0122e78249b29278ef', 'S'),
(8, 'mani', 'manita@gmail.com', 'pbkdf2:sha256:600000$39gabGBPvzmZP6bI$7fb9f40ad8ae19e2a183ce8f4dbd3749f798b5fea810b73ec215fed39e06da2f', 'S'),
(28, 'mani', 'valeria.avalos1717@alumnos.udg.mx', 'pbkdf2:sha256:600000$bOeTlNpuYNa7oVXU$8a830d56c2c45f60254d49e5de3704830905cedb085d28a23a5f3b6232a5977a', 'S'),
(31, 'el pedillos', 'garciajarethisaac@gmail.com', 'pbkdf2:sha256:600000$Ec8hdRgF3QlmV2iV$e585696b57f31909541bd5ef31f7cfc2303301cf7b7cc1b339397a8f4e3b6ec1', 'S'),
(32, 'Adan', 'adan.lopez6589@academicos.udg.mx', 'pbkdf2:sha256:600000$1kvJkxzdz6ySR8kT$65958505d2e1d470bc19a9837fc4627a76ef7ea99d69b5739d878f4503f4ac46', 'S');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cancion`
--
ALTER TABLE `cancion`
  ADD PRIMARY KEY (`idcancion`);

--
-- Indices de la tabla `inserta`
--
ALTER TABLE `inserta`
  ADD PRIMARY KEY (`idinserta`),
  ADD KEY `idcancion` (`idcancion`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correou` (`correou`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cancion`
--
ALTER TABLE `cancion`
  MODIFY `idcancion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `inserta`
--
ALTER TABLE `inserta`
  MODIFY `idinserta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `inserta`
--
ALTER TABLE `inserta`
  ADD CONSTRAINT `inserta_ibfk_1` FOREIGN KEY (`idcancion`) REFERENCES `cancion` (`idcancion`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
