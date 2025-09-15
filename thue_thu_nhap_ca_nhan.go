package main
import "fmt"

func thue_tncn(lương_gross int, số_người_phụ_thuộc int) (int, int) {
	return lương_gross, số_người_phụ_thuộc
}

func main() {
	fmt.Println("Bạn có thể nhập số tiền bằng phân cách bằng dấu ',' , ví dụ : 10,000,000")
	fmt.Println("~ ---------- ~")
	var lương_gross int
	var số_người_phụ_thuộc int
	fmt.Scan(&lương_gross)
	fmt.Scan(&số_người_phụ_thuộc)
	var result, result2 = thue_tncn(lương_gross, số_người_phụ_thuộc)
	fmt.Println(result, result2)
}