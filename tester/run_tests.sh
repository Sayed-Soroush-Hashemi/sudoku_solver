# create input files list
cd inputs
file_names=()
for file_name in *.txt
do
	file_names+=($file_name)
done
cd ..

# compile c++ program
g++ ../sudoku_solver.cpp -O2 -o cpp_sudoku_solver.out

# run solver
rm outputs/*
for file_name in ${file_names[@]}
do 
	./cpp_sudoku_solver.out < "inputs/$file_name" > "outputs/$file_name"
done

# check outputs
python check_outputs.py
