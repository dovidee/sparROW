data Gruppe:
  | group(
      id :: String)
  | requires(
      mentor :: Boolean)
end

data Student:
  | noInfo
  | person(
      name :: String,
      birthyear :: Number,
      group :: Gruppe)
  | owner(
      student-id :: Boolean
      )
end

group-1B = group("1-B")
group-2B = group("2-B")
group-3B = group("3-B")

student-john = person("John", 2000, group-1B)
student-jane = person("Jane", 1999, group-2B)
student-gary = person("Gary", 1990, group-3B)

fun check-group(student-type :: Student, group-number :: String) -> Boolean:
  cases (Student) student-type:
    | noInfo => false
    | person(n, b, g) => check-group(g, group)
  end
where:
  student-john.group is group("1-B")
  student-jane.group is group("2-B")
  student-gary.group is group("3-B")
end
