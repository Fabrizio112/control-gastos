from src import control_gastos_app

app=control_gastos_app()

if __name__ =="__main__":
    app.run(debug=True,port=5000)