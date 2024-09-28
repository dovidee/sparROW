# Dette er feil oppgave

include gdrive-sheets
include tables
include math
include chart
import tables as T
import lists as L
include data-source

cleaned-sheet = load-spreadsheet("1FJK4K0NH_yYP1F3pq2VaZvr03TedSgR_VRwVyzdSn38")
cleaned-table = load-table: Sted :: Number, Y2015 :: Number, Y2016 :: Number, Y2017 :: Number, Y2018 :: Number, Y2019 :: Number, Y2020 :: Number, Y2021 :: Number, Y2022 :: Number, Y2023 :: Number source: cleaned-sheet.sheet-by-name("oppgave2", true)
  sanitize Sted using string-sanitizer
  sanitize Y2015 using num-sanitizer
  sanitize Y2016 using num-sanitizer
  sanitize Y2017 using num-sanitizer
  sanitize Y2018 using num-sanitizer
  sanitize Y2019 using num-sanitizer
  sanitize Y2020 using num-sanitizer
  sanitize Y2021 using num-sanitizer
  sanitize Y2022 using num-sanitizer
  sanitize Y2023 using num-sanitizer
end


Sted = cleaned-table.get-column("Sted")
Y2015 = cleaned-table.get-column("Y2015")
Y2016 = cleaned-table.get-column("Y2016")
Y2017 = cleaned-table.get-column("Y2017")
Y2018 = cleaned-table.get-column("Y2018")
Y2019 = cleaned-table.get-column("Y2019")
Y2020 = cleaned-table.get-column("Y2020")
Y2021 = cleaned-table.get-column("Y2021")
Y2022 = cleaned-table.get-column("Y2022")
Y2023 = cleaned-table.get-column("Y2023")

fun highest(list1, list2):
  tested = map2(lam(elt1, elt2):
      if elt2 == max(list2):
        elt1
      else:
        ""
      end
    end, list1, list2)
  filter(lam(elt3): not(elt3 == "") end, tested)
end

fun lowest(list1, list2):
  nullbye = filter(lam(elt): elt > 0 end, list2)
  tested = map2(lam(elt1, elt2):
      if elt2 == min(nullbye):
        elt1
      else:
        ""
      end
    end, list1, list2)
  filter(lam(elt3): not(elt3 == "") end, tested)
end
