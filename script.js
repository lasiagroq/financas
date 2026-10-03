const cart = [];
const cartPanel = document.querySelector('#cartPanel');
const scrim = document.querySelector('#scrim');
const cartItems = document.querySelector('#cartItems');
const cartCount = document.querySelector('#cartCount');
const cartTotal = document.querySelector('#cartTotal');
const checkout = document.querySelector('#checkout');
const toast = document.querySelector('#toast');

const money = (value) => value.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

function toggleCart(show) {
  cartPanel.classList.toggle('open', show);
  scrim.classList.toggle('show', show);
  cartPanel.setAttribute('aria-hidden', String(!show));
}

function renderCart() {
  const total = cart.reduce((sum, item) => sum + item.price, 0);
  cartCount.textContent = cart.length;
  cartTotal.textContent = money(total);
  checkout.disabled = cart.length === 0;
  cartItems.innerHTML = cart.length
    ? cart.map((item, index) => `<div class="cart-item"><div><h3>${item.name}</h3><p>${money(item.price)}</p></div><button data-remove="${index}">Remover</button></div>`).join('')
    : '<p class="empty">Sua sacola está vazia.<br>Que tal escolher uma marmita?</p>';
}

document.querySelectorAll('.add').forEach((button) => button.addEventListener('click', () => {
  cart.push({ name: button.dataset.name, price: Number(button.dataset.price) });
  renderCart();
  toast.classList.add('show');
  window.setTimeout(() => toast.classList.remove('show'), 1800);
}));

cartItems.addEventListener('click', (event) => {
  const index = event.target.dataset.remove;
  if (index !== undefined) { cart.splice(Number(index), 1); renderCart(); }
});
document.querySelector('#cartButton').addEventListener('click', () => toggleCart(true));
document.querySelector('#closeCart').addEventListener('click', () => toggleCart(false));
scrim.addEventListener('click', () => toggleCart(false));
document.querySelectorAll('.filter').forEach((button) => button.addEventListener('click', () => {
  document.querySelectorAll('.filter').forEach((filter) => filter.classList.remove('active'));
  button.classList.add('active');
  document.querySelectorAll('.dish').forEach((dish) => { dish.hidden = button.dataset.filter !== 'todos' && dish.dataset.category !== button.dataset.filter; });
}));
checkout.addEventListener('click', () => alert('Obrigada! Vamos confirmar os detalhes do seu pedido pelo WhatsApp.'));
