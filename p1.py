"""Solves problem 1 of Project Euler"""
def sum_divisible_by_n(n, target=999):
	p = target/n
	return (n*p*(p+1))/2

if __name__=='__main__':
	print sum_divisible_by_n(3) + sum_divisible_by_n(5) - sum_divisible_by_n(15)
