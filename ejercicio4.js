const orders = [
  { id: 1, total: 50, paid: true },
  { id: 2, total: 30, paid: false },
  { id: 3, total: 70, paid: true },
];

function procesar_pedidos(orders) {
  const totalPaid = orders.reduce((acc, order) => {
    return order.paid ? acc + order.total : acc;
  }, 0);

  const unpaidIds = orders
    .filter(order => !order.paid)
    .map(order => order.id);

  return { totalPaid, unpaidIds };
}

const result = procesar_pedidos(orders);
console.log(result);