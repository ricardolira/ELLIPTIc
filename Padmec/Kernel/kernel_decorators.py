
def preprocess(vector_name=""):

    def dec(kernel_class):
        if not vector_name:
            kernel_class.name = kernel_class.__name__
        else:
            kernel_class.name = vector_name

        orig_run = kernel_class.run

        @classmethod
        def run(cls, elem, adj, mb):
            orig_run(elem, adj, mb)

        @classmethod
        def create_array(cls, matrix_manager):
            matrix_manager.create_vector(
                kernel_class.solution_dim, kernel_class.name)

        kernel_class.run = run
        kernel_class.create_array = create_array
        return kernel_class

    return dec


def fill_matrix(matrix_name=""):

    def dec(kernel_class):
        if not matrix_name:
            kernel_class.name = kernel_class.__name__
        else:
            kernel_class.name = matrix_name

        orig_run = kernel_class.run

        @classmethod
        def run(cls, elem, adj, mb):
            orig_run(elem, adj, mb)

        @classmethod
        def create_array(cls, matrix_manager):
            matrix_manager.create_matrix(
                kernel_class.solution_dim, kernel_class.name)

        kernel_class.run = run
        kernel_class.create_array = create_array
        return kernel_class

    return dec
