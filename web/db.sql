-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: pukulenam
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `key`
--

DROP TABLE IF EXISTS `key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `key` (
  `id` int NOT NULL AUTO_INCREMENT,
  `masterPassword` varchar(50) DEFAULT NULL,
  `apiKey` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `key`
--

LOCK TABLES `key` WRITE;
/*!40000 ALTER TABLE `key` DISABLE KEYS */;
INSERT INTO `key` VALUES (1,'pukulenam','0fa082af97380ffdecee051edb6b0b80');
/*!40000 ALTER TABLE `key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `inputNews` text,
  `summarizedNews` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (2,' Menteri Keuangan (Menkeu) Sri Mulyani menegaskan inflasi Indonesia yang tercatat 3,5 persen pada Mei 2022 lebih baik dari Turki dan Mesir.\r\nDalam pertemuan Islamic Development Bank di Mesir pekan ini, ia bertemu dengan banyak menteri keuangan dari seluruh dunia, termasuk Turki dan Mesir yang sama-sama bercerita mengenai tekanan inflasi di negara masing-masing.\r\n\r\nIa mengungkapkan Turki tengah menghadapi situasi yang sulit karena inflasinya melonjak tajam hingga 74 persen di Mei 2022. Hal ini dipicu karena tidak ada subsidi untuk menekan kenaikan harga energi.','Intinyaa...  bernama jerman telepon diterima kebudayaan ular bocoran bank keesokan barang barang milik juni media partai'),(4,'Selama tahun 2014-2019, jumlah subsidi BBM mencapai Rp700 triliun. Di APBN 2021, subsidi untuk BBM jenis tertentu mencapai Rp16,6 triliun,lanjutnya.Bamsoet menilai potensi pengembangan kendaraan listrik di Indonesia sangat menjanjikan. Terlebih, di tengah kesuksesan pelaksanaan Formula E Sabtu kemarin.Dalam road map pengembangan kendaraan bermotor listrik berbasis baterai yang disusun Kementerian Energi dan Sumber Daya Mineral, potensi sepeda motor listrik pada 2030 diproyeksikan mencapai 13 juta unit, sedangkan mobil listrik mencapai 2,2 juta unit, kata Bamsoet.',' pemerintah tua dihadiri pikirkan timur pemerintah indonesia minggu 06 08 pembunuhan psikologis'),(5,'Harga jual emas PT Aneka Tambang (Persero) Tbk atau Antam tercatat Rp981 ribu per gram pada Rabu (8/6). Harga emas ini naik Rp5.000 dari Rp976 ribu per gram pada perdagangan hari sebelumnya.Sejalan, harga pembelian kembali (buyback) juga ikut naik Rp5.000 dari sebelumnya Rp855 ribu per gram menjadi Rp860 ribu per gram pada hari ini.Berdasarkan data Antam, harga jual emas berukuran 0,5 gram senilai Rp540,5 ribu, 2 gram Rp1,902 juta, 3 gram Rp2,828 juta, 5 gram Rp4,68 juta, 10 gram Rp9,305 juta, 25 gram Rp23,137 juta, dan 50 gram Rp46,195 juta.','Intinyaa...  menteri negara negara al penurunan sri pemerintah korea laki ahli apapun uji coba perang berasal'),(6,'Kemudian, harga emas berukuran 100 gram senilai Rp92,312 juta, 250 gram Rp230,515 juta, 500 gram Rp460,82 juta, dan 1 kilogram Rp921,6 juta.\r\n\r\nHarga jual emas tersebut sudah termasuk Pajak Penghasilan (PPh) 22 atas emas batangan sebesar 0,45 persen bagi pemegang Nomor Pokok Wajib Pajak (NPWP). Sedangkan, pembeli yang tidak menyertakan NPWP dikenakan potongan pajak lebih tinggi sebesar 0,9 persen.\r\n\r\nSementara itu, harga emas di perdagangan internasional berdasarkan acuan pasar Commodity Exchange COMEX naik 0,06 persen menjadi US$1.853,2 per troy ons. Sedangkan harga emas di perdagangan spot turun 0,08 persen ke US$1.850,98 per troy ons pada pagi ini.','Intinyaa...  nama remaja kulit hitam peserta korea laki rugi daftar hitam pesawat diduga jatuh reuters terpasang'),(7,'Pengamat Komoditas Ariston Tjendra memprediksi kenaikan harga emas akan berlanjut pada hari ini. Hal tersebut dipicu oleh hasil laporan Bank Dunia mengenai stagflasi.\r\n\r\n\"Jadinya pergerakan naik harga emas bisa tertahan,\" ujarnya kepada CNNIndonesia.\r\n\r\nSelain itu, isu kenaikan suku bunga oleh Bank Sentral Amerika Serikat (the Fed) yang mencuat juga menjadi sentimen positif terhadap harga emas.\r\n\r\nOleh karenanya, Ariston melihat harga emas hari ini bisa melaju naik ke arah US$1870 per troy ons','Intinyaa...  pemerintah celah selama kawasan kawasan ilmu barat pertukaran penjara penularan sungai senin 26 terbaru'),(9,'Pemerintah dan DPR telah menyepakati Peraturan Komisi Pemilihan Umum (PKPU) tentang Jadwal dan Tahapan Pemilihan Umum (Pemilu) 2024 dalam rapat dengar pendapat di Komisi II DPR, Selasa (7/6) malam.\r\nDalam aturan itu, pemungutan suara akan digelar pada 14 Februari 2024. PKPU juga mengatur sejumlah proses lain mulai dari pendaftaran, verifikasi peserta pemilu, hingga masa kampanye.','Intinyaa...  \'\' maaf akses bantuan pemerintah sipil wilayah beruang cina agama elektronik mati polisi bahagia'),(10,'Polemik tentang khilafah kembali mencuat di Indonesia. Penyebabnya, konvoi rombongan bermotor membawa panji khilafah di wilayah Jakarta beberapa waktu lalu yang berujung penangkapan pemimpin Khilafatul Muslimin, Abdul Qadir Baraja.\r\nResidivis terorisme itu ditangkap personel Polda Metro Jaya di wilayah Lampung pada awal pekan ini. Kabid Humas Polda Metro Jaya Kombes E. Zulpan menyampaikan penangkapan Baraja tak sekadar didasari aksi konvoi khilafah yang digelar di Cawang, Jakarta Timur pada 29 Mei lalu.\r\n\r\n\"Namun sebuah kegiatan yang tidak terpisahkan dari provokasi yang diucapkan dengan ucapan kebencian serta berita bohong yang dilakukan dengan menjelekkan pemerintah yang sah, pemerintah yang saat ini ada di negara kita,\" kata Zulpan dalam konferensi pers, Selasa (7/6).\r\n\r\n\r\n\"Kemudian kelompok ini menawarkan khilafah sebagai solusi pengganti ideologi negara demi kemakmuran bumi dan kesejahteraan umat,\" lanjutnya yang menyatakan itu bertentangan dengan UUD 1945.','Intinyaa...  indonesia peraih fosil petani mendesak majalah josua dinyatakan aksi dunia bertemu kebudayaan olimpiade'),(11,' Badan Pusat Statistik (BPS) mencatat Indonesia mengimpor 20 jenis alat kesehatan (alkes) senilai US$1,45 miliar sepanjang Januari hingga April 2022.\r\nMengutip data BPS, Rabu (8/6), RI mengimpor alkes sebanyak 33.347 ton sejak awal tahun sampai akhir April 2022.\r\n\r\nLebih rinci, Indonesia mengimpor pembersih tangan alias hand sanitizer sebanyak 2.479 ton, bahan baku hand sanitizer 38.629 ton, produk mengandung disinfektan 4.381 ton, alat rapid test 91,445 ton, alat PCR tes 2.932 ton, virus transfer media 1.513 ton, serta obat dan vitamin 5.124 ton. ','Intinyaa...  konser kebanyakan dinyatakan arab juru bertekad asumsi berkarya darurat menteri cenderung negara'),(12,'\"A man is believed to have driven into a group of people. It is not yet known whether it was an accident or a deliberate act,\" police said on Twitter, adding that the driver was being held at the scene.\r\nCablitz said that the driver is now being questioned.\r\nMore than 130 emergency services personnel are at the scene, Berlin\'s mayor Franziska Giffey said in a post on Twitter, thanking them for their quick response. Videos shared on social media showed a helicopter arriving at the scene.','Intinyaa...  nama remaja kulit hitam elektronik mati milik anak anak berputar penghasilan \''),(13,' Harga telur ayam kian dekati Rp30 ribu per kg di DKI Jakarta. pada Kamis (9/6).\r\nMengutip situs infopangan.jakarta.co.id, harga telur ayam Rp29.606 per kg, atau naik Rp63 dari kemarin.\r\nKenaikan harga ini hampir terjadi di seluruh daerah. \r\nMengutip pusat informasi harga pangan strategis (PIHPS) nasional, Kamis (9/6), rata-rata nasional harga telur ras segar mencapai Rp29.400 per kg.\r\n\r\nHarga telur ayam ras segar terendah ada di Sulawesi Barat dan Sulawesi Selatan Rp24.350 ribu per kg.\r\n\r\nHarga telur ayam tertinggi ada di Maluku dan Papua masing-masing Rp39.350 per kg dan Rp39.100 per kg.\r\n\r\nDi Jawa Timur, harga telur ayam dibanderol Rp27.600 per kg. Di Jawa Tengah Rp28.100 per kg dan di Jawa Barat dijual Rp29.100 per kg.','Intinyaa...  pemerintah inggris kyi amerika serikat nasir thailand memasang foto foto delhi menambah asing warga air');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-13 14:53:15
