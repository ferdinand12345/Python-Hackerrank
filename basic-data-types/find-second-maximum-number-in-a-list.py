if __name__ == '__main__':
	n = int(input())
	arr = map(int, input().split())
	
	# Hapus elemen yang duplikat, biar tersisa nilai unik
	unique_arr = list(set(arr))

	# Mengurutkan list secara descending
	unique_arr.sort(reverse=True)
	xxx = unique_arr[1]

	print(xxx)