#!/usr/bin/ruby
=begin
Code Ruby dùng để tính thuế thu nhập cá nhân, nhập vào lương chưa khấu trừ + số người phụ thuộc
=end

def format_with_thousand_delimiters(number_string)
  reversed = number_string.reverse
  # Use gsub to insert commas every 3 digits
  formatted = reversed.gsub(/(\d{3})(?=\d)/, '\1,').reverse
  return formatted
end

def thue_tncn(lương_gross,số_người_phụ_thuộc)

=begin
  Hàm tính thuế thu nhập cá nhân bằng Ruby
=end

  thue = 0
  lương_gross = lương_gross
  số_người_phụ_thuộc = số_người_phụ_thuộc
  bh_tổng = lương_gross * 10.5 / 100
  lương_net = lương_gross - bh_tổng
  thu_nhập_tính_thuế = lương_net - 11000000> 0 ? lương_net - 11000000 : 0
  if thu_nhập_tính_thuế <= 0
    thuế = 0
  else
    case thu_nhập_tính_thuế
      when (0..5000000+1) #Bậc thuế 5%
        thuế = thu_nhập_tính_thuế *5/100 - 4400000*số_người_phụ_thuộc
      when (5000000..10000000+1) #Bậc thuế 10%
        thuế = 250000 + (thu_nhập_tính_thuế-5000000)*10/100 - 4400000*số_người_phụ_thuộc
      when (10000000..18000000+1) #Bậc thuế 15%
        thuế = 750000 + (thu_nhập_tính_thuế-10000000)*15/100 - 4400000*số_người_phụ_thuộc
      when (18000000..32000000+1) #Bậc thuế 20%
        thuế = 1950000 + (thu_nhập_tính_thuế-18000000)*20/100 - 4400000*số_người_phụ_thuộc
      when (32000000..52000000) #Bậc thuế 25%
        thuế = 4750000 + (thu_nhập_tính_thuế-32000000)*25/100 - 4400000*số_người_phụ_thuộc
      when (52000000..80000000+1) #Bậc thuế 30%
        thuế = 9750000 + (thu_nhập_tính_thuế-52000000)*30/100 - 4400000*số_người_phụ_thuộc
      else
        thuế = 18150000 + (thu_nhập_tính_thuế-80000000)*35/100 - 4400000*số_người_phụ_thuộc
    end
  end
  print("-----------------------------------\n")
  return bh_tổng.round(),lương_net.round(),thu_nhập_tính_thuế.round(),thuế > 0 ? thuế.round() : 0,
      thuế > 0 ? (lương_net - thuế.round()).round() : 0
end

if __FILE__ == $0
  # puts "Bạn có thể nhập số tiền bằng phân cách bằng dấu ',' , ví dụ : 10,000,000"
  puts "Nhập lương Gross "
  lương_gross = Integer(gets.chomp, exception: false)
  print "Nhập số người phụ thuộc : \n"
  số_người_phụ_thuộc = Integer(gets.chomp, exception: false)
  bh_tổng,lương_net,thu_nhập_tính_thuế,thuế,còn_lại = thue_tncn(lương_gross,số_người_phụ_thuộc)
  puts "Bảo hiểm cần đóng là: #{format_with_thousand_delimiters(bh_tổng.to_s)} Đồng"
  puts "lương net là: #{format_with_thousand_delimiters(lương_net.to_s)} Đồng"
  puts "Thu nhập tính thuế là: #{format_with_thousand_delimiters(thu_nhập_tính_thuế.to_s)} Đồng"
  puts "Vậy thuế thu nhập cá nhân bạn cần đóng là: #{format_with_thousand_delimiters(thuế.to_s)} Đồng"
  if  còn_lại > 0
    puts("-----------------------------------")
    puts("Sau khi đóng thuế TNCN, bạn còn lại #{format_with_thousand_delimiters(còn_lại.to_s)} Đồng")
  end
end
