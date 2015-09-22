import string
p = b''

p1 = open('1','rb').read()
p2 = open('2','rb').read()
p3 = open('3','rb').read()
p += bytes([p1[i]^p3[i] for i in range(min(len(p1),len(p3)))])
c = """YPSILANTI, eight miles distant from Ann Arbor, is the next stopping
place, and is a pleasant town of some five thousand inhabitants. The
fine water power of Huron River is here utilized by several
manufactories, among which that of paper-making is brought to a high
state of excellence. In addition to the railroad facilities afforded by
the Michigan Central, it has southerly communication by means of a
branch of the Lake Shore & Michigan Southern Railway. It is the seat of
the State Normal School, which occupies an elegant building, and
beautiful grounds, the latter donated to the State for the purpose.
There are many fine residences here, some of them the homes of business
men of Detroit.

[Illustration: STATE NORMAL SCHOOL.]

The Roberts, Lewis, and Hawkins Houses, the European, and several
others, furnish adequate hotel accommodations.

From Ypsilanti, the train speeds swiftly over the smoothest of tracks,
past pleasant villages, through verdant fields, and in view of snug
farm-houses, the next important stopping places being WAYNE JUNCTION,
where connection is made with the Flint & Pere Marquette Railroad, and
SPRINGWELLS, formerly Grand Trunk Junction, three miles beyond which is


DETROIT, THE CITY OF THE STRAIT.

The largest city in Michigan, and its commercial metropolis, it is
beautifully situated on the Detroit River, 18 miles from Lake Erie, and
7 from Lake St. Clair. It is one of the prettiest, pleasantest cities in
all the West, and the oldest, as well. Its rapid growth during the past
twenty years is a marked feature in connection with its history. The
many lines of railroad centering here, and its extensive commercial
interests, together with the rich agricultural region which here finds
an outlet for its products, all contribute to the prosperity of the
city.

The excursionist will find much to interest in a visit to Detroit. Its
location upon the river, which is here about half a mile wide, suggests
excursions by water, which constitute a considerable share of the
recreation of its people, by the numerous lines of steamers which ply
between the city and various points on the river and the lakes. The
public parks of the city afford pleasant â\x80\x9cbreathing placesâ\x80\x9d for those
who choose to avail themselves of their advantages. In addition to the
older resorts of this class, the city has recently purchased Belle Isle,
with an area of abou"""

c = """The River Rats used the cave as headquarters, and for a long time afterward would
suddenly sally forth from the concealment of the hole and surprise
and beat any strange lad who was incautious enough to venture in the
neighborhood unprotected by a company of friends. This adventure taught
us several things, and one night, at the “dark of the moon,” we met in
a smoke-house and formed ourselves into a secret society. Over a bottle
of strained honey we made solemn vows, and the secrets of the society
have never been divulged until now.

The name, the purpose, and the fact of there being any society were the
three great secrets. The name was “The Three Ancient Mariners.” The
object was to stand by each other to the crack of doom, and the seal,
3??A??M, was tattooed on each member???s good right arm.

The vows were religiously"""

c = c.replace("“","â\x80\x9c").replace("”","â\x80\x9d")
c = c.encode('cp500')
l = []
# "se and formed ourselves into a secret society" " communication by means of a\nbranch of the La"
# "ade constant" " through ver"
# " appear" "s, the "
# " five thousand inhabitants " "om the concealment of the c"
for i in range(len(p)-len(c)):
    dec = bytes([p[i+j]^c[j] for j in range(len(c))]).decode('cp500')
    if sum([1 for j in dec if j in string.printable]) >= len(c)-20:
        print(i,"'"+dec+"'")
