class ModuloPedidos:
    def __init__(self):
        self.pedidos = []

    def crear(self, id_prod, catalogo):
        # En lugar de buscar en su propia memoria, 
        # le pregunta al objeto 'catalogo' que le pasamos
        if catalogo.validar_existencia(id_prod):
            nuevo = {"id": len(self.pedidos) + 1, "prod_id": id_prod}
            self.pedidos.append(nuevo)
            return True, nuevo
        return False, None