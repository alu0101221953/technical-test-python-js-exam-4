class Switch {
  constructor() {
    this.state = false;
  }

  toggle() {
    this.state = !this.state;
    return this.state ? "On" : "Off";
  }
}

const mySwitch = new Switch();
console.log(mySwitch.toggle()); // Encendido
console.log(mySwitch.toggle()); // Apagado
console.log(mySwitch.toggle()); // Encendido
console.log(mySwitch.toggle()); // Apagado