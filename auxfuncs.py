def getCountyName(lookup_number):
  county_numbers_dict = {"Adams" : "14",
  "Antelope" : "26",
  "Arthur" : "91",
  "Banner" : "85",
  "Blaine" : "86",
  "Boone" : "23",
  "Box Butte" : "65",
  "Boyd" : "63",
  "Brown" : "75",
  "Buffalo" : "09",
  "Burt" : "31",
  "Butler" : "25",
  "Cass" : "20",
  "Cedar" : "13",
  "Chase" : "72",
  "Cherry" : "66",
  "Cheyenne" : "39",
  "Clay" : "30",
  "Colfax" : "43",
  "Cuming" : "24",
  "Custer" : "04",
  "Dakota" : "70",
  "Dawes" : "69",
  "Dawson" : "18",
  "Deuel" : "78",
  "Dixon" : "35",
  "Dodge" : "05",
  "Douglas" : "01",
  "Dundy" : "76",
  "Fillmore" : "34",
  "Franklin" : "50",
  "Frontier" : "60",
  "Furnas" : "38",
  "Gage" : "03",
  "Garden" : "77",
  "Garfield" : "83",
  "Gosper" : "73",
  "Grant" : "92",
  "Greeley" : "62",
  "Hall" : "08",
  "Hamilton" : "28",
  "Harlan" : "51",
  "Hayes" : "79",
  "Hitchcock" : "67",
  "Holt" : "36",
  "Hooker" : "93",
  "Howard" : "49",
  "Jefferson" : "33",
  "Johnson" : "57",
  "Kearney" : "52",
  "Keith" : "68",
  "Keya Paha" : "82",
  "Kimball" : "71",
  "Knox" : "12",
  "Lancaster" : "02",
  "Lincoln" : "15",
  "Logan" : "87",
  "Loup" : "88",
  "Madison" : "07",
  "McPherson" : "90",
  "Merrick" : "46",
  "Morrill" : "64",
  "Nance" : "58",
  "Nemaha" : "44",
  "Nuckolls" : "42",
  "Otoe" : "11",
  "Pawnee" : "54",
  "Perkins" : "74",
  "Phelps" : "37",
  "Pierce" : "40",
  "Platte" : "10",
  "Polk" : "41",
  "Red Willow" : "48",
  "Richardson" : "19",
  "Rock" : "81",
  "Saline" : "22",
  "Sarpy" : "59",
  "Saunders" : "06",
  "Scotts Bluff" : "21",
  "Seward" : "16",
  "Sheridan" : "61",
  "Sherman" : "56",
  "Sioux" : "80",
  "Stanton" : "53",
  "Thayer" : "32",
  "Thomas" : "89",
  "Thurston" : "55",
  "Valley" : "47",
  "Washington" : "29",
  "Wayne" : "27",
  "Webster" : "45",
  "Wheeler" : "84",
  "York" : "17"}
  for key, value in county_numbers_dict.items():
    if lookup_number == value:
      return key  
  return "no such county"

def getOffsets(numResults, limitPerPage):
  offsetsList = []
  number_of_offsets = int(int(numResults)/limitPerPage) + 1
  for x in range(number_of_offsets):
    offsetsList.append(x * limitPerPage)
  return offsetsList