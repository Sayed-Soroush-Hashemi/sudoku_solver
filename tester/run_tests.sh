# create input files list
cd inputs
file_names=()
for file_name in *.txt
do
	file_names+=($file_name)
done
cd ..

case $1 in
	"cpp" ) 
		g++ ../sudoku_solver.cpp -O2 -o cpp_sudoku_solver.out
		program="./cpp_sudoku_solver.out"
		;;
	"python" )
		program="python ../sudoku_solver.py"
		;;
esac

rm outputs/*
for file_name in ${file_names[@]}; do 
	$program < "inputs/$file_name" > "outputs/$file_name"
done

# check outputs
python check_outputs.py
