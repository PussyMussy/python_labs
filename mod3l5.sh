PROGRAM_FILE="mod2/l7.py"
PYLINT_OUTPUT="pylint_report.json"

echo "Запуск анализатора pylint..."
pylint --output-format=json "$PROGRAM_FILE" > "$PYLINT_OUTPUT"
pylres=$?

if [[ $pylres -eq 0 ]]; then
    echo "Pylint OK"
else
    echo "Pylint ERR"
fi

cat "$PYLINT_OUTPUT"

echo "Запуск тестов..."
python3 -m unittest discover -s . -p "mod3l3.py"
tres=$?

if [[ $tres -eq 0 && $pylres -eq 0 ]]; then
    echo "ОК"
else
    echo "ERR"
fi

rm -f "$PYLINT_OUTPUT"