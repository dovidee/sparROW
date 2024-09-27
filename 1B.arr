data Gruppe:
  | group(
      id :: String)
  | owns(# Sjekk om gruppen har mentor
      mentor :: Boolean)
end

data Student:
  | noInfo
  | person(
      name :: String,
      birthyear :: Number,
      group :: Gruppe)
  | owner( # Sjekk om student eier ID
      student-id :: Boolean
      )
end

# Lag grupper med id
group-1B = group("1-B")
group-2B = group("2-B")
group-3B = group("3-B")

# Lag personer med navn, fødselsdato, og gruppe
student-john = person("John", 2000, group-1B)
student-jane = person("Jane", 1999, group-2B)
student-gary = person("Gary", 1990, group-3B)

fun check-group(student-type :: Student, group-number :: String) -> Boolean:
  doc: "Tar et person og gruppenummer som input for å se om den tilhører gruppen"
  cases (Student) student-type:
    | noInfo => false # Returner falsk hvis tom data
    | person(n, b, g) => check-group(g, group) # Returner true hvis gruppen stemmer
  end
where: # Alle 3 tester funker
  student-john.group is group("1-B")
  student-jane.group is group("2-B")
  student-gary.group is group("3-B")
end
