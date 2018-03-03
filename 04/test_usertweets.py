from collections import namedtuple
import csv
import datetime
import unittest
from unittest.mock import patch

from usertweets import UserTweets, NUM_TWEETS

Tweet = namedtuple('Tweet', ['id_str', 'created_at', 'text'])
HANDLE = 'pybites'
MAX_ID = '819831370113351680'

# Here we have 100 tweets for the above settings
TWEETS = (Tweet(id_str='819831370113351680', created_at=datetime.datetime(2017, 1, 13, 9, 0, 5), text='5 cool things you can do with itertools https://t.co/Nk4s3yL6zL #python'),
Tweet(id_str='819682682703593472', created_at=datetime.datetime(2017, 1, 12, 23, 9, 15), text='RT @bbelderbos: https://t.co/P4aX1vIUUC - heard of itertools? If not you might want to check it out, can do some cool things with it ... #p…'),
Tweet(id_str='819469028678725633', created_at=datetime.datetime(2017, 1, 12, 9, 0, 16), text='Cheat Sheet: Python For Data Science https://t.co/pqhepaavl1 #python'),
Tweet(id_str='819468986978971648', created_at=datetime.datetime(2017, 1, 12, 9, 0, 6), text='#94 Guarenteed packages via Conda and Conda-Forge https://t.co/6pKEQ9t89J #python'),
Tweet(id_str='819468975922786304', created_at=datetime.datetime(2017, 1, 12, 9, 0, 3), text='Create a Simple Web Scraper with BeautifulSoup4 https://t.co/PY4JSvWIZw #python'),
Tweet(id_str='819441364429668352', created_at=datetime.datetime(2017, 1, 12, 7, 10, 20), text="RT @mkennedy: Cool presentation: 10 awesome features of Python that you can't use because you refuse to upgrade to Python 3 https://t.co/3z…"),
Tweet(id_str='819106611025166336', created_at=datetime.datetime(2017, 1, 11, 9, 0, 8), text='Comprehending Python’s Comprehensions https://t.co/we9hO354uv #python'),
Tweet(id_str='819106605920702464', created_at=datetime.datetime(2017, 1, 11, 9, 0, 7), text='#8 Python gets Grumpy, avoiding burnout, Postman for API testing and more https://t.co/rSLt7q7g8S #python'),
Tweet(id_str='819106595531464705', created_at=datetime.datetime(2017, 1, 11, 9, 0, 5), text='#94 Guarenteed packages via Conda and Conda-Forge https://t.co/6pKEQ9t89J #python'),
Tweet(id_str='819106588057161728', created_at=datetime.datetime(2017, 1, 11, 9, 0, 3), text='Beautiful, idiomatic Python https://t.co/Gft5OaBkon #python'),
Tweet(id_str='819083179629936641', created_at=datetime.datetime(2017, 1, 11, 7, 27, 2), text='https://t.co/s5rEdcKZin talk about #data and #nlp, so cool we can watch all #pycon videos online, such a great way to learn'),
Tweet(id_str='819082820329017346', created_at=datetime.datetime(2017, 1, 11, 7, 25, 36), text="I love the key on max, min, sorted, so powerful and concise. Also using it in this week's coding challenge :) https://t.co/vpL1R3bSIW"),
Tweet(id_str='819082265674285056', created_at=datetime.datetime(2017, 1, 11, 7, 23, 24), text='@kennethreitz same feeling yesterday :)'),
Tweet(id_str='819076605918248960', created_at=datetime.datetime(2017, 1, 11, 7, 0, 55), text='RT @kennethreitz: Taught someone Python today. Feels good :)'),
Tweet(id_str='818951461782646788', created_at=datetime.datetime(2017, 1, 10, 22, 43, 38), text='RT @getpy: Generators https://t.co/vF2lHX3D6Q by the author of the fluent python. #generators'),
Tweet(id_str='818947474236862464', created_at=datetime.datetime(2017, 1, 10, 22, 27, 47), text='RT @PythonWeekly: chatbot-rnn - A toy chatbot powered by deep learning and trained on data from Reddit. https://t.co/a6rIpINOHy #python'),
Tweet(id_str='818898348312850433', created_at=datetime.datetime(2017, 1, 10, 19, 12, 35), text='RT @_ericelliott: The best code is no code. Where there is no code, there are no bugs. No API to learn. No awkward UI. The best refactors a…'),
Tweet(id_str='818885175719370752', created_at=datetime.datetime(2017, 1, 10, 18, 20, 14), text='RT @PythonWeekly: PEP8 Speaks - A GitHub integration which checks pep8 issues and then comments over Pull Requests. https://t.co/WyjrwR5YUo…'),
Tweet(id_str='818840038729535488', created_at=datetime.datetime(2017, 1, 10, 15, 20, 53), text='RT @TrendingGithub: pybites / challenges: Repo for our weekly challenges on pybit.es ★28 https://t.co/U1pFa7kucO #Python'),
Tweet(id_str='818744285180751873', created_at=datetime.datetime(2017, 1, 10, 9, 0, 23), text='Iterators https://t.co/n3MXkT0Gr3 #python'),
Tweet(id_str='818744209863675904', created_at=datetime.datetime(2017, 1, 10, 9, 0, 5), text='Code Challenge 01 - Word Values Part I https://t.co/h4N81Ll6ZC #python'),
Tweet(id_str='818744208156561410', created_at=datetime.datetime(2017, 1, 10, 9, 0, 5), text='Beautiful, idiomatic Python https://t.co/Gft5OaBkon #python'),
Tweet(id_str='818740548664168449', created_at=datetime.datetime(2017, 1, 10, 8, 45, 32), text='@PyPiglesias @bedjango thx for sharing. Nice to see folks jumping on it! We comment possible solutions and learning on Friday ...'),
Tweet(id_str='818734200035614720', created_at=datetime.datetime(2017, 1, 10, 8, 20, 19), text='refactor ugly switch statement in #python https://t.co/2Plq0XHVAu'),
Tweet(id_str='818544004467978240', created_at=datetime.datetime(2017, 1, 9, 19, 44, 33), text='Like this video https://t.co/CmKKSbXKhE'),
Tweet(id_str='818537299629764609', created_at=datetime.datetime(2017, 1, 9, 19, 17, 54), text='RT @fullstackpython: Working with APIs the Pythonic Way https://t.co/TQyVxcO5yw'),
Tweet(id_str='818535072143970305', created_at=datetime.datetime(2017, 1, 9, 19, 9, 3), text='RT @newsycombinator: Show HN: PyBites Code Challenges https://t.co/0Z2ro5q5Qk'),
Tweet(id_str='818398781372829696', created_at=datetime.datetime(2017, 1, 9, 10, 7, 29), text='PyBites of the Week - https://t.co/Lynq8vE7Tb'),
Tweet(id_str='818392237847511040', created_at=datetime.datetime(2017, 1, 9, 9, 41, 29), text='RT @python_alc: Desafíos en #Python 🐍 cada lunes. El primero, buscar la palabra con mayor puntuación de Scrabble de un fichero dado \nhttps:…'),
Tweet(id_str='818381812397314048', created_at=datetime.datetime(2017, 1, 9, 9, 0, 3), text='Code Challenge 01 - Word Values Part I https://t.co/h4N81Ll6ZC #python'),
Tweet(id_str='818356383926128640', created_at=datetime.datetime(2017, 1, 9, 7, 19), text="@Duvancarrez we're a new blog rather. We added challenges as we think they are a fun and great way to learn more Python."),
Tweet(id_str='818224729035329537', created_at=datetime.datetime(2017, 1, 8, 22, 35, 51), text='Time for a #python code challenge!  \n\nCode Challenge 01 - Word Values Part I   \n\nhttps://t.co/h4N81L3w84 https://t.co/lnvYc6xJXG'),
Tweet(id_str='818019426091999232', created_at=datetime.datetime(2017, 1, 8, 9, 0, 3), text='Twitter digest 2017 week 01 https://t.co/lRZrfmB9QN #python'),
Tweet(id_str='817835538908581888', created_at=datetime.datetime(2017, 1, 7, 20, 49, 21), text='RT @nedbat: Python tip: get nicer output in the repl:  &gt;&gt;&gt; sys.displayhook = pprint.pprint;   Add to your PYTHONSTARTUP file'),
Tweet(id_str='817746028560584705', created_at=datetime.datetime(2017, 1, 7, 14, 53, 40), text='RT @gcosma1: The entire Python Data Science Handbook by @jakevdp is openly published as Jupyter notebook https://t.co/w7RKk5IaC8 https://t.…'),
Tweet(id_str='817745548409245696', created_at=datetime.datetime(2017, 1, 7, 14, 51, 46), text='https://t.co/WZ4lad2oJv - go running python'),
Tweet(id_str='817657038268485632', created_at=datetime.datetime(2017, 1, 7, 9, 0, 3), text='Copy and Paste with Pyperclip https://t.co/6CNbUpCWw4 #python'),
Tweet(id_str='817657037127454722', created_at=datetime.datetime(2017, 1, 7, 9, 0, 3), text='Twitter digest 2017 week 01 https://t.co/lRZrfmB9QN #python'),
Tweet(id_str='817635389922013184', created_at=datetime.datetime(2017, 1, 7, 7, 34, 2), text='RT @dbader_org: Python Package 101 https://t.co/DrNeBsAWCP'),
Tweet(id_str='817635169213579264', created_at=datetime.datetime(2017, 1, 7, 7, 33, 9), text='I got Python Tricks: The Book (Work-In-Progress) from @dbader_org on @Gumroad: https://t.co/U54ZyzTEa0'),
Tweet(id_str='817477174253023237', created_at=datetime.datetime(2017, 1, 6, 21, 5, 20), text='RT @dataelixir: Looking for data? Follow @CoolDatasets for curated datasets that are open and machine-readable.'),
Tweet(id_str='817443042823176193', created_at=datetime.datetime(2017, 1, 6, 18, 49, 43), text='RT @codeorg: Learning to code at age 56 :-) https://t.co/qsY8Ydu8J8'),
Tweet(id_str='817442461673017344', created_at=datetime.datetime(2017, 1, 6, 18, 47, 24), text='RT @dbader_org: I just published another update for the early access version of my new book. Grab the updated PDF and ePub today 🙂 https://…'),
Tweet(id_str='817394424518950913', created_at=datetime.datetime(2017, 1, 6, 15, 36, 31), text='@techmoneykids challenge, recreate this graph ... https://t.co/hQ0SziiQDv'),
Tweet(id_str='817356740253675520', created_at=datetime.datetime(2017, 1, 6, 13, 6, 47), text='RT @pydatait: The next PyData Italy will be again hosted by the Python Italian Conference @pyconit in Florence https://t.co/EfYhVamr3j #pyd…'),
Tweet(id_str='817354773292871680', created_at=datetime.datetime(2017, 1, 6, 12, 58, 58), text="RT @treyhunner: #pythontip: whenever you see range(len(fancy_list)), pause to consider which problem you're solving\nhttps://t.co/hw6poTSJUv…"),
Tweet(id_str='817294653745602560', created_at=datetime.datetime(2017, 1, 6, 9, 0, 4), text='Code Challenge #01 - code review https://t.co/UjR3G68eSq #python'),
Tweet(id_str='817280745861484544', created_at=datetime.datetime(2017, 1, 6, 8, 4, 48), text='The ultimate list of #Python #Podcasts https://t.co/fqPkqS3zva - nice list'),
Tweet(id_str='817145648680144896', created_at=datetime.datetime(2017, 1, 5, 23, 7, 59), text='RT @NicolasDular: "It\'s really important to have hobbies other than writing code." https://t.co/dmsAO8t9YH great post from @kennethreitz ab…'),
Tweet(id_str='817132674112516101', created_at=datetime.datetime(2017, 1, 5, 22, 16, 25), text='https://t.co/szO1tTdMre good explanation of iterators and iterables'),
Tweet(id_str='817100263425196037', created_at=datetime.datetime(2017, 1, 5, 20, 7, 38), text="RT @tarek_ziade: Excited to share that I've started a book about building microservices using Python - https://t.co/QRZFLFeaeQ"),
Tweet(id_str='816932292799000577', created_at=datetime.datetime(2017, 1, 5, 9, 0, 11), text='#7 Python 3.6 is out, Sanic is a blazing web framework, and are failing our open source infrastructure? https://t.co/1632fQa3xU #python'),
Tweet(id_str='816932263673753600', created_at=datetime.datetime(2017, 1, 5, 9, 0, 4), text='Challenge: Course Total Time Web Scraper https://t.co/RTwa15021s #python'),
Tweet(id_str='816764531594657792', created_at=datetime.datetime(2017, 1, 4, 21, 53, 33), text="RT @pythonbytes: It's @pythonbytes #7: Python 3.6 is out, Sanic is a blazing web framework, and failing open source infrastructure? https:/…"),
Tweet(id_str='816701767928971265', created_at=datetime.datetime(2017, 1, 4, 17, 44, 9), text="RT @CAChemEorg: If one of your New Year's resolutions is learning a bit more of Python, check Pybite.es out!  cc @pybites https://t.co/rnO8…"),
Tweet(id_str='816701515503173633', created_at=datetime.datetime(2017, 1, 4, 17, 43, 9), text='@CAChemEorg thanks for the share, happy New Year'),
Tweet(id_str='816569933202997248', created_at=datetime.datetime(2017, 1, 4, 9, 0, 17), text='Python 3.5.3rc1 and Python 3.4.6rc1 are now available https://t.co/8XP5CWH6XF #python'),
Tweet(id_str='816569887313117184', created_at=datetime.datetime(2017, 1, 4, 9, 0, 6), text='#93 Spreading Python through the sciences with Software Carpentry https://t.co/38EBc45KL9 #python'),
Tweet(id_str='816569873673269248', created_at=datetime.datetime(2017, 1, 4, 9, 0, 3), text='A great book that makes algorithms accessible https://t.co/2tkf4ZWiJA #python'),
Tweet(id_str='816555347674595328', created_at=datetime.datetime(2017, 1, 4, 8, 2, 20), text='interesting #python #dict https://t.co/BTXxPWNYVc https://t.co/9d1RgcrhXK'),
Tweet(id_str='816545953268305920', created_at=datetime.datetime(2017, 1, 4, 7, 25), text='RT @newsafaribooks: Building RESTful Python Web Services #PacktPublishing https://t.co/eBJ1Oqxvul #Python'),
Tweet(id_str='816539053097185280', created_at=datetime.datetime(2017, 1, 4, 6, 57, 35), text='RT @treyhunner: #pythontip: Whenever you find yourself considering using a lambda in #Python, think about whether you should make a named f…'),
Tweet(id_str='816382171619454976', created_at=datetime.datetime(2017, 1, 3, 20, 34, 12), text='One of my favorite programming quotes #cleancode https://t.co/qzDrzKgdq5'),
Tweet(id_str='816381754319589376', created_at=datetime.datetime(2017, 1, 3, 20, 32, 32), text='@_egonschiele ML, more confident tackling it after your book, maybe idea for part II? (Applying algorithms to ML problems)'),
Tweet(id_str='816369304702685184', created_at=datetime.datetime(2017, 1, 3, 19, 43, 4), text="RT @PyDataMallorca: We start 2017 with a challenge. If we get 30 tweets about #PyDataMallorca, we'll have @PyData stickers for all assisten…"),
Tweet(id_str='816207547589763072', created_at=datetime.datetime(2017, 1, 3, 9, 0, 18), text='Python 3.5.3rc1 and Python 3.4.6rc1 are now available https://t.co/8XP5CWH6XF #python'),
Tweet(id_str='816207520079310849', created_at=datetime.datetime(2017, 1, 3, 9, 0, 11), text='How to Write Regularly for Your Programming Blog https://t.co/fbUCU1do5v #python'),
Tweet(id_str='816207495362277376', created_at=datetime.datetime(2017, 1, 3, 9, 0, 5), text='5 min guide to PEP8 https://t.co/8LoAzqBqvT #python'),
Tweet(id_str='816207494166953984', created_at=datetime.datetime(2017, 1, 3, 9, 0, 5), text='Book that makes algorithms accessible https://t.co/2tkf4ZWiJA #python'),
Tweet(id_str='816170167575134208', created_at=datetime.datetime(2017, 1, 3, 6, 31, 46), text='RT @newsafaribooks: Data Pipelines with Python #InfiniteSkills https://t.co/iXKS3GMrb6 #Python'),
Tweet(id_str='816170147270590464', created_at=datetime.datetime(2017, 1, 3, 6, 31, 41), text='RT @newsafaribooks: Modern Python Cookbook #PacktPublishing https://t.co/ODsSdGXNSG #Python'),
Tweet(id_str='816170103876255744', created_at=datetime.datetime(2017, 1, 3, 6, 31, 31), text='#python #excel https://t.co/lGuSaOFaio'),
Tweet(id_str='815853681648271360', created_at=datetime.datetime(2017, 1, 2, 9, 34, 10), text='https://t.co/Dko7iUWysc Pybites weekly newsletter! Our latest posts on one handy page. Keep Calm and Code in #Python!'),
Tweet(id_str='815845096839004160', created_at=datetime.datetime(2017, 1, 2, 9, 0, 3), text='Python Naming Conventions https://t.co/P3ox8A01D3 #python'),
Tweet(id_str='815482716946722816', created_at=datetime.datetime(2017, 1, 1, 9, 0, 5), text='3.6 new features https://t.co/6atEam0H9i #python'),
Tweet(id_str='815150151685783552', created_at=datetime.datetime(2016, 12, 31, 10, 58, 35), text='@Pybonacci violaciones mas dramaticas?'),
Tweet(id_str='815120360756641792', created_at=datetime.datetime(2016, 12, 31, 9, 0, 12), text="RT @PacktPub: It's back. And it's simple. Every single eBook and every single video on our site is now $5. #packt5dollar https://t.co/8R4Ls…"),
Tweet(id_str='815120322890338304', created_at=datetime.datetime(2016, 12, 31, 9, 0, 3), text="Don't Let Indentation Catch You Out https://t.co/u2iR5XPKXS #python"),
Tweet(id_str='815096989172068352', created_at=datetime.datetime(2016, 12, 31, 7, 27, 20), text='3 best #python books https://t.co/fDYkPZ07S7'),
Tweet(id_str='815095206479560704', created_at=datetime.datetime(2016, 12, 31, 7, 20, 15), text='RT @jbeda: New term: "Technology Stockholm Syndrome" \n\nThis is when a technology sucks but you are way too involved to see it. We all fall…'),
Tweet(id_str='814957152746008576', created_at=datetime.datetime(2016, 12, 30, 22, 11, 41), text='@TalkPython @_egonschiele thanks for this episode and book, flying through it, finally a book that makes algorithms easy to grasp. Great job'),
Tweet(id_str='814956683088818177', created_at=datetime.datetime(2016, 12, 30, 22, 9, 49), text='RT @TalkPython: Announcing @talkpython #82: Grokking Algorithms in Python with @_egonschiele https://t.co/j7Zl39lE6j https://t.co/TYbjSr0LVw'),
Tweet(id_str='814956287586947073', created_at=datetime.datetime(2016, 12, 30, 22, 8, 14), text='RT @TalkPython: My new sounds: #86: Python at StackOverflow https://t.co/OG8EZ47Ob7 on #SoundCloud'),
Tweet(id_str='814955307218731009', created_at=datetime.datetime(2016, 12, 30, 22, 4, 21), text='@dbader_org loved automate boring, fluent py takes you to the next level. Also liked powerful python, mastering py. Started expert py 2nd ed'),
Tweet(id_str='814817662974959616', created_at=datetime.datetime(2016, 12, 30, 12, 57, 24), text='“Boot Up 2017 with the #100DaysOfCode Challenge” @ka11away https://t.co/LLJkOWpGDt'),
Tweet(id_str='814757951311200256', created_at=datetime.datetime(2016, 12, 30, 9, 0, 7), text='#92 Bonus: Python Bytes Crossover: Python 3.6 is going to be awesome, Kite: your friendly co-developing AI https://t.co/0gazCa1EpZ #python'),
Tweet(id_str='814503909154758656', created_at=datetime.datetime(2016, 12, 29, 16, 10, 39), text='RT @ShowHNDaily: PyBites – sharing our passion for Python, one bite a day. https://t.co/RNWFvBLgfp'),
Tweet(id_str='814395545774981120', created_at=datetime.datetime(2016, 12, 29, 9, 0, 3), text='Automate Tweeting: how to build a Twitterbot https://t.co/y75ZCLBJaB #python'),
Tweet(id_str='814077436379860992', created_at=datetime.datetime(2016, 12, 28, 11, 56), text='The Difference Between “is” and “==” in Python https://t.co/6HCZugHkQS #python'),
Tweet(id_str='814077424388349952', created_at=datetime.datetime(2016, 12, 28, 11, 55, 57), text='#91 Top 10 Data Science Stories of 2016 https://t.co/Aao9ZJFLW8 #python'),
Tweet(id_str='814077411318870016', created_at=datetime.datetime(2016, 12, 28, 11, 55, 54), text='Learning from Python mistakes https://t.co/hPWVXt21p7 #python'),
Tweet(id_str='814048629740761088', created_at=datetime.datetime(2016, 12, 28, 10, 1, 32), text='RT @pythonbytes: Time for the final @pythonbytes of 2016: #6: Python 3.6 is going to be awesome, Kite: your friendly co-developing AI https…'),
Tweet(id_str='814041751577133056', created_at=datetime.datetime(2016, 12, 28, 9, 34, 12), text='RT @gvanrossum: Yes! Python 3.6.0 (final) is released!!! https://t.co/DIWDxoUuXd Thanks @baybryj and all core devs, contributors and beta t…'),
Tweet(id_str='814038105602789376', created_at=datetime.datetime(2016, 12, 28, 9, 19, 43), text='RT @PythonWeekly: Python Weekly - Issue 275 https://t.co/N4mcWU0Ajz #python #django #flask #tensorflow #pandas #raspberrpi #pycharm #docker'),
Tweet(id_str='814022779473448960', created_at=datetime.datetime(2016, 12, 28, 8, 18, 49), text='RT @dbader_org: I started a YouTube channel with screencasts for Python devs » https://t.co/3Kakis45pv 🎥 Tell me what you think &amp; subscribe…'),
Tweet(id_str='814022376568537088', created_at=datetime.datetime(2016, 12, 28, 8, 17, 13), text='one place for all #python videos, awesome - https://t.co/QgxtrlNtwW'),
Tweet(id_str='814021637637017600', created_at=datetime.datetime(2016, 12, 28, 8, 14, 16), text='RT @TalkPython: Announcing @TalkPython #90: Data Wrangling with Python with @kjam https://t.co/j42MKzWxYb https://t.co/lbMgX9iy0z'),
Tweet(id_str='813535741049503744', created_at=datetime.datetime(2016, 12, 27, 0, 3, 30), text='How to create a nice-looking HTML page of your #Kindle book highlights (notes) https://t.co/HKFK7inhUa #python'),
Tweet(id_str='813517244487581696', created_at=datetime.datetime(2016, 12, 26, 22, 50), text='RT @guyfig: Just before 2016 is ending, here is a great answer from last week by Zuck.  @mkennedy @TalkPython #Python #devops https://t.co/…'),
Tweet(id_str='813366158359404544', created_at=datetime.datetime(2016, 12, 26, 12, 49, 38), text='#vim #python environment https://t.co/WFzvrdQX5j'),
)

def read_csv(fname):
    with open(fname) as f:
        has_header = csv.Sniffer().has_header(f.readline())
        f.seek(0)
        r = csv.reader(f)
        if has_header:
            next(r, None)  # skip the header
        return [Tweet(id_str=tw[0], created_at=tw[1], text=tw[2]) for tw in r]  # list(r)


class TestUserTweets(unittest.TestCase):
    def setUp(self):
        super().setUp()
        with patch('tweepy.API.user_timeline') as mock_timeline:
            mock_timeline.return_value = TWEETS
            self.user = UserTweets(HANDLE, max_id=MAX_ID)

    def tearDown(self):
        self.user = None
        super().tearDown()

    def test_num_tweets(self):
        self.assertEqual(len(self.user), NUM_TWEETS)

    def test_first_tweet_returned_by_api(self):
        tw_n = 0
        self.assertEqual(self.user[tw_n].id_str, MAX_ID)
        self.assertEqual(self.user[tw_n].created_at, TWEETS[tw_n].created_at)
        self.assertEqual(self.user[tw_n].text, TWEETS[tw_n].text)

    def test_read_back_from_cached_csv(self):
        csv_tweets = read_csv(self.user.output_file)
        self.assertEqual(len(csv_tweets), NUM_TWEETS)
        tw_n = 0  # first
        self.assertEqual(csv_tweets[tw_n].id_str, MAX_ID)
        self.assertEqual(csv_tweets[tw_n].created_at, str(TWEETS[tw_n].created_at))
        self.assertEqual(csv_tweets[tw_n].text, TWEETS[tw_n].text)
        tw_n = -1  # last
        self.assertEqual(csv_tweets[tw_n].text, TWEETS[tw_n].text)


if __name__ == "__main__":
    unittest.main()
