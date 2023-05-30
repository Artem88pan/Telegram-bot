def select(input_func):
    def output_func():
        print('я выполнился до функции')
        input_func()
        print('я выполнился послк функции')