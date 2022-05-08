import random
import time

from otree.api import *


author = 'Your name here'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'count_words'
    players_per_group = None
    num_rounds = 2
    payment_per_round = 10
    my_file = ['ablasi', 'abrasi', 'absurd', 'adegan', 'aditif', 'adopsi', 'aerasi', 'aerial', 'afasia', 'agresi',
               'akasia', 'aksara', 'aksial', 'akting', 'aktiva', 'alamat', 'alegro', 'aliran', 'alkali', 'aluran',
               'ambang', 'ambing', 'analis', 'anemia', 'anggar', 'anggur', 'angkat', 'angket', 'angkut', 'angsur',
               'anjing', 'anjung', 'anomik', 'antara', 'antena', 'anting', 'apitan', 'aqabah', 'aramea', 'arheis',
               'arisan', 'arjuna', 'asabat', 'asetat', 'asmara', 'astral', 'asupan', 'atrisi', 'aturan', 'aurora',
               'avokad', 'awetan', 'babala', 'bagasi', 'bagian', 'bagong', 'bahang', 'bahari', 'bahasa', 'bahaya',
               'bailey', 'bajang', 'bajing', 'bakung', 'balang', 'balita', 'balong', 'balsam', 'bancah', 'bandar',
               'bandut', 'bangau', 'banget', 'bangka', 'bangsa', 'bangun', 'banjar', 'banjir', 'bantal', 'banyak',
               'baptis', 'barang', 'barter', 'batang', 'batton', 'bawaan', 'bawang', 'begitu', 'belang', 'benalu',
               'benang', 'bencet', 'bendul', 'bensin', 'bentuk', 'benzil', 'beradu', 'berahi', 'berapi', 'bercak',
               'berita', 'berkas', 'berkat', 'beroda', 'bersih', 'bersin', 'bestir', 'betina', 'biawak', 'bicara',
               'bidang', 'bidara', 'bilhal', 'bilmal', 'biotik', 'birama', 'bisnis', 'blanko', 'bodong', 'bohong',
               'boikot', 'bolong', 'bombai', 'boneka', 'bonsai', 'brahmi', 'bridge', 'brisan', 'buatan', 'budaya',
               'bujana', 'bujang', 'bulang', 'bumban', 'buncis', 'bundar', 'bungsu', 'buntal', 'buntut', 'burpee',
               'burung', 'busana', 'busung', 'butbut', 'cabang', 'cacing', 'cahaya', 'cairan', 'cakram', 'cambuk',
               'campak', 'campur', 'candik', 'caping', 'carang', 'caveat', 'cawiri', 'cedera', 'cekung', 'celana',
               'cerdas', 'cerdik', 'cerita', 'cermat', 'cermin', 'cincin', 'contoh', 'corong', 'corpus', 'cuping',
               'daerah', 'dafnah', 'daftar', 'dagang', 'daging', 'dahaga', 'dahagi', 'dakwah', 'daling', 'dampit',
               'daring', 'daulat', 'dayung', 'delima', 'demdem', 'dendam', 'dengar', 'desain', 'dewata', 'dialek',
               'dialog', 'diesel', 'difusi', 'dingin', 'dokter', 'dolman', 'dolore', 'domain', 'dompet', 'donang',
               'dorong', 'drajat', 'dugong', 'duktus', 'dulang', 'durian', 'duyung', 'eceran', 'editor', 'efluen',
               'ejekan', 'ekonom', 'ekspor', 'elemen', 'embrio', 'eminen', 'empati', 'empedu', 'emptor', 'energi',
               'epolet', 'erotik', 'estrus', 'fabula', 'faktor', 'faktur', 'faring', 'filter', 'foniks', 'formal',
               'format', 'franca', 'fundus', 'fungsi', 'gading', 'gagang', 'galang', 'galeri', 'gamang', 'gambar',
               'gambir', 'gambut', 'gangan', 'gaplek', 'garang', 'garing', 'gawang', 'gebeng', 'gedung', 'gegana',
               'gejala', 'geladi', 'gelang', 'geleng', 'gelung', 'gembel', 'genjah', 'gereja', 'gerigi', 'gering',
               'gertak', 'gesing', 'giling', 'ginjal', 'giring', 'global', 'goreng', 'gotong', 'grafik', 'gratia',
               'gratis', 'grelin', 'gubang', 'gudang', 'gulana', 'guling', 'gulung', 'gumpal', 'gundah', 'gundal',
               'gundik', 'gundul', 'guntur', 'gunung', 'guring', 'habeas', 'hablur', 'hadley', 'haluan', 'hampir',
               'handuk', 'hangat', 'hanyut', 'harian', 'haribu', 'hasrat', 'hayati', 'heliks', 'hendak', 'herbal',
               'hernia', 'heroik', 'herpes', 'hiatal', 'hidang', 'hidung', 'hilang', 'hormon', 'hubung', 'humbut',
               'hunian', 'ibarat', 'ijazah', 'ikutan', 'ilegal', 'ilmiah', 'impian', 'indeks', 'ingkar', 'insang',
               'intern', 'intrik', 'isapan', 'jagung', 'jalang', 'jamban', 'jamrah', 'jamuan', 'jangan', 'janggi',
               'jangka', 'jantan', 'jaring', 'jayeng', 'jelata', 'jemaat', 'jempol', 'jenaka', 'jenang', 'jenawi',
               'jengki', 'jepang', 'jerkat', 'jermal', 'jerman', 'jernih', 'jinawi', 'jojoba', 'jovian', 'juling',
               'kabihu', 'kabuki', 'kacang', 'kahrab', 'kalang', 'kaleng', 'kalong', 'kalori', 'kalung', 'kamera',
               'kampak', 'kanada', 'kancil', 'kanola', 'kantor', 'kapita', 'karang', 'karbit', 'karbon', 'karier',
               'karkas', 'karpal', 'karpet', 'kasasi', 'kasren', 'kastor', 'kasual', 'kawung', 'kecoak', 'kejang',
               'kelapa', 'kelasi', 'kelian', 'kelima', 'keling', 'keluai', 'keluar', 'kembar', 'kembul', 'kemeja',
               'kemiri', 'kemudi', 'kencur', 'kendur', 'kening', 'kental', 'kentar', 'kentum', 'kenyah', 'kepada',
               'kepala', 'kerang', 'kerapu', 'kerbau', 'kerdol', 'keremi', 'kereta', 'kering', 'kermak', 'kernet',
               'kerong', 'kertas', 'keruit', 'ketang', 'ketela', 'ketiak', 'khuldi', 'khusus', 'kiasan', 'kidang',
               'kidung', 'kijang', 'kilang', 'kimono', 'kincai', 'kincir', 'kiting', 'kiwalu', 'klasik', 'klinik',
               'klinis', 'klutuk', 'kobiwi', 'kohesi', 'koloid', 'kolone', 'kolong', 'koloni', 'kombor', 'komedi',
               'komidi', 'komisi', 'komite', 'kompak', 'kompas', 'kompor', 'kontak', 'kontes', 'kontra', 'kopral',
               'kopyor', 'korona', 'korpus', 'kosmin', 'kosong', 'kostum', 'kotong', 'kowibi', 'krasak', 'kredit',
               'krisis', 'kritik', 'kritis', 'kronis', 'kuaran', 'kuboid', 'kucing', 'kudung', 'kumkum', 'kuncup',
               'kuning', 'kuntul', 'kupang', 'kuping', 'kurang', 'kurban', 'kuring', 'kursus', 'kurung', 'kustar',
               'kusuma', 'labora', 'ladang', 'lading', 'laguna', 'laktat', 'lalang', 'lamban', 'lambat', 'lancar',
               'lancip', 'lancor', 'landak', 'landas', 'langis', 'langit', 'langur', 'lanjut', 'lantai', 'lantak',
               'laring', 'lateks', 'latung', 'lawina', 'layang', 'lebong', 'lector', 'leding', 'lektor', 'lelang',
               'lemari', 'lembam', 'lembap', 'lembar', 'lembek', 'lembur', 'lembut', 'lempar', 'lenang', 'lengan',
               'lengas', 'lenyap', 'leping', 'lereng', 'lesung', 'letnan', 'leuser', 'limbah', 'limbik', 'limbuk',
               'lincir', 'linear', 'lingga', 'lingua', 'lintas', 'liofob', 'logika', 'lokasi', 'lompat', 'loncat',
               'lontar', 'lontok', 'lorong', 'losong', 'loyang', 'lubang', 'lumpuh', 'lumpur', 'lunggi', 'lupung',
               'luteum', 'mahfuz', 'mainan', 'makmum', 'malang', 'malela', 'manado', 'mancur', 'mandah', 'mandor',
               'mangga', 'manila', 'manset', 'mantri', 'marapi', 'markah', 'markas', 'marmet', 'martil', 'masbuk',
               'masker', 'master', 'matang', 'materi', 'mayang', 'medium', 'melaba', 'melati', 'melayu', 'melian',
               'meluar', 'memori', 'menang', 'menara', 'mendam', 'meniru', 'meniti', 'menkeh', 'menkop', 'menkum',
               'mentah', 'mental', 'mentik', 'merang', 'merapi', 'merbau', 'mereka', 'meriam', 'merkel', 'mersik',
               'merugi', 'metode', 'miller', 'minded', 'minyak', 'miring', 'miskin', 'mistar', 'modern', 'monyet',
               'moyang', 'muatan', 'mundur', 'musang', 'museum', 'muslim', 'musnah', 'mutasi', 'mutlak', 'nabati',
               'nagari', 'napalm', 'naskah', 'nebula', 'negara', 'negeri', 'neraca', 'neraka', 'neroli', 'netral',
               'ngarai', 'nisbah', 'nomina', 'nontes', 'normal', 'nuklir', 'nutfah', 'nyatuh', 'oklusi', 'olahan',
               'olakan', 'ompong', 'oolong', 'operan', 'opioid', 'opname', 'opstal', 'oregon', 'otonom', 'pabean',
               'pabrik', 'padang', 'pagoda', 'pakpak', 'palazo', 'paling', 'palkah', 'palolo', 'palung', 'pancah',
               'pancal', 'pancar', 'pancur', 'pandai', 'pandak', 'pandan', 'pangan', 'pangek', 'pangsi', 'pangus',
               'panjat', 'pantai', 'pantas', 'pantat', 'pantul', 'pantun', 'parade', 'parang', 'parket', 'parkir',
               'parsel', 'partai', 'pasang', 'pasien', 'pasiva', 'paspor', 'passim', 'pasung', 'patria', 'patuha',
               'patung', 'pawang', 'payung', 'pedang', 'peking', 'pelaku', 'peluit', 'peluru', 'pemain', 'pemuda',
               'pemula', 'penata', 'pendar', 'pendek', 'peniup', 'pensil', 'pentas', 'pepaku', 'peraga', 'perahu',
               'perang', 'pereka', 'pergam', 'periuk', 'permen', 'pernis', 'pesagi', 'petani', 'phalen', 'pidana',
               'pigmen', 'pinang', 'pindah', 'pindai', 'pining', 'pintar', 'pintas', 'piring', 'pisang', 'pistol',
               'planet', 'plasma', 'pletok', 'pocong', 'polder', 'polisi', 'polong', 'pondok', 'ponjen', 'ponsel',
               'posisi', 'postur', 'potehi', 'potong', 'potret', 'priayi', 'primer', 'produk', 'profil', 'prokem',
               'proses', 'protes', 'publik', 'puding', 'pulang', 'pungut', 'pusaka', 'pusing', 'puteri', 'rabung',
               'radang', 'radial', 'raglan', 'rahani', 'rakyat', 'rambat', 'rambun', 'rambut', 'rampai', 'randah',
               'ranjau', 'ransel', 'ransum', 'rantah', 'rantai', 'rantau', 'reaksi', 'realis', 'rejang', 'rekaan',
               'relief', 'religi', 'relung', 'remaja', 'rendah', 'rentan', 'retina', 'rezeki', 'rimpel', 'ringan',
               'risiko', 'rohani', 'romawi', 'rongga', 'rotasi', 'royong', 'rubber', 'rumpun', 'rumput', 'runtuh',
               'sadang', 'sading', 'sakura', 'sambal', 'sambao', 'sampah', 'sampai', 'sampul', 'sanang', 'sandai',
               'sandal', 'sangat', 'sangga', 'sangit', 'santai', 'santri', 'sapaan', 'sarang', 'saring', 'sarung',
               'sasana', 'sastra', 'satire', 'satuan', 'sawang', 'sayang', 'sebaju', 'seblat', 'secang', 'sedang',
               'segala', 'seguna', 'sehari', 'sehina', 'sekain', 'sekaya', 'sekket', 'sekrup', 'sektor', 'sekutu',
               'selada', 'selama', 'selang', 'selera', 'seluar', 'semalu', 'semata', 'sembah', 'semeru', 'sempit',
               'semula', 'sendok', 'senduk', 'sengal', 'sengir', 'senior', 'sensor', 'sentak', 'sentuh', 'senyum',
               'sepata', 'sepatu', 'sepeda', 'septik', 'sepupu', 'seraga', 'serang', 'serani', 'serbuk', 'sersan',
               'seruas', 'serupa', 'servis', 'setali', 'setang', 'seteru', 'seumur', 'sewaan', 'siagha', 'sianok',
               'siasat', 'sibela', 'sidang', 'sikari', 'siklon', 'siklus', 'silang', 'simpai', 'simpuh', 'simpul',
               'simpur', 'sintar', 'sinyal', 'sirene', 'sistem', 'sitaan', 'sitasi', 'slamet', 'sokong', 'sollen',
               'sondek', 'sorong', 'sosial', 'specie', 'spiral', 'stabil', 'statis', 'status', 'sterol', 'strata',
               'subang', 'suling', 'sultan', 'sulung', 'sumber', 'sumpah', 'sumsum', 'sundal', 'sundul', 'sundut',
               'sungai', 'suntuk', 'supaya', 'surung', 'susila', 'syajar', 'tablet', 'tabrak', 'tabung', 'takluk',
               'talang', 'talkin', 'tambak', 'tambul', 'tampal', 'tampuk', 'tancap', 'tandem', 'tandon', 'tanduk',
               'tangan', 'tangga', 'tangki', 'target', 'taruna', 'tarung', 'tarzan', 'teater', 'tebang', 'tebing',
               'tedung', 'teknik', 'teknis', 'telaah', 'temara', 'tembak', 'tembok', 'tembus', 'tempat', 'tempel',
               'tempur', 'tenaga', 'tenang', 'tengah', 'tepung', 'terang', 'terapi', 'terasi', 'terbit', 'terima',
               'terjun', 'termal', 'ternak', 'terner', 'teruna', 'timbul', 'timbun', 'timpas', 'tindak', 'tinggi',
               'tinjau', 'tipuan', 'togata', 'toilet', 'toksik', 'toksin', 'tombak', 'tombol', 'topeng', 'trayek',
               'trofik', 'tromol', 'tropik', 'tropis', 'tuanku', 'tubruk', 'tudung', 'tujuan', 'tukang', 'tukung',
               'tulang', 'tumang', 'tumbuh', 'tumbuk', 'tumpak', 'tumpas', 'tunang', 'tunggu', 'tungku', 'tunjuk',
               'ucapan', 'ukiran', 'ukuran', 'ulasan', 'ulayat', 'uluran', 'undang', 'unggas', 'unggun', 'untung',
               'usikan', 'usiran', 'verbal', 'visual', 'voyage', 'walang', 'wanita', 'warkat', 'wasiat', 'wayang',
               'wedang', 'welter', 'wicara', 'wisata', 'yasmin', 'yenimu', 'yunani', 'zaitun', 'zoster']


class Player(BasePlayer):
    word1 = models.FloatField()
    word2 = models.FloatField()
    word3 = models.FloatField()
    word4 = models.FloatField()
    word5 = models.FloatField()
    word6 = models.FloatField()
    word7 = models.FloatField()
    word8 = models.FloatField()
    word9 = models.FloatField()
    word10 = models.FloatField()
    answer1 = models.FloatField()
    answer2 = models.FloatField()
    answer3 = models.FloatField()
    answer4 = models.FloatField()
    answer5 = models.FloatField()
    answer6 = models.FloatField()
    answer7 = models.FloatField()
    answer8 = models.FloatField()
    answer9 = models.FloatField()
    answer10 = models.FloatField()



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass




# FUNCTIONS
# PAGES
class AddNumbers(Page):
    timeout_seconds = 60
    form_model = "player"
    form_fields = ["word1", "word2", "word3", "word4", "word5", "word6", "word7", "word8", "word9", "word10"]
    @staticmethod
    def vars_for_template(player: Player):
        txt = Constants.my_file
        word_1 = random.choice(txt)
        word_2 = random.choice(txt)
        word_3 = random.choice(txt)
        word_4 = random.choice(txt)
        word_5 = random.choice(txt)
        word_6 = random.choice(txt)
        word_7 = random.choice(txt)
        word_8 = random.choice(txt)
        word_9 = random.choice(txt)
        word_10 = random.choice(txt)
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        count7 = 0
        count8 = 0
        count9 = 0
        count10 = 0
        list = ["A", "I", "U", "E", "O", "a", "i", "u", "e", "o"]
        #word 1
        for char in word_1:
            if char in list:
                count1 += 1
        #word2
        for char2 in word_2:
            if char2 in list:
                count2 += 1
        #word3
        for char4 in word_3:
            if char4 in list:
                count3 += 1
        #word4
        for char4 in word_4:
            if char4 in list:
                count4 += 1
        # word5
        for char5 in word_5:
            if char5 in list:
                count5 += 1
        #word6
        for char6 in word_6:
            if char6 in list:
                count6 += 1
        #word7
        for char7 in word_7:
            if char7 in list:
                count7 += 1
        #word8
        for char8 in word_8:
            if char8 in list:
                count8 += 1
        #word9
        for char9 in word_9:
            if char9 in list:
                count9 += 1
        #word10
        for char10 in word_10:
            if char10 in list:
                count10 += 1

        player.answer1 = count1
        player.answer2 = count2
        player.answer3 = count3
        player.answer4 = count4
        player.answer5 = count5
        player.answer6 = count6
        player.answer7 = count7
        player.answer8 = count8
        player.answer9 = count9
        player.answer10 = count10
        return {
            "word_1": word_1,
            "word_2": word_2,
            "word_3": word_3,
            "word_4": word_4,
            "word_5": word_5,
            "word_6": word_6,
            "word_7": word_7,
            "word_8": word_8,
            "word_9": word_9,
            "word_10": word_10,
        }
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.word1 == player.answer1 and player.word2 == player.answer2 and player.word3 == player.answer3 and player.word4 == player.answer4 and player.word5 == player.answer5 and player.word6 == player.answer6 and player.word7 == player.answer7 and player.word8 == player.answer8 and player.word9 == player.answer9 and player.word10 == player.answer10:
            player.payoff = Constants.payment_per_round


class Results(Page):
    pass


class CombinedResults(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    @staticmethod
    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        combined_payoff = 0
        for player in all_players:
            combined_payoff += player.payoff
        return {"combined_payoff": combined_payoff}


page_sequence = [AddNumbers, Results, CombinedResults]
