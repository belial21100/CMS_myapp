import { useState } from 'react';

export default function Home() {
  const [metal, setMetal] = useState(100);
  const [energy, setEnergy] = useState(100);
  const [naquadah, setNaquadah] = useState(50);
  const [fleet, setFleet] = useState(0);
  const [turn, setTurn] = useState(0);

  function buildMine() {
    const cost = 20;
    if (metal >= cost) {
      setMetal(metal - cost);
      setEnergy(energy + 10);
    } else {
      alert('Pas assez de metal');
    }
  }

  function buildShip() {
    const costMetal = 30;
    const costNaquadah = 10;
    if (metal >= costMetal && naquadah >= costNaquadah) {
      setMetal(metal - costMetal);
      setNaquadah(naquadah - costNaquadah);
      setFleet(fleet + 1);
    } else {
      alert('Ressources insuffisantes');
    }
  }

  function nextTurn() {
    setTurn(turn + 1);
    setMetal(metal + 10);
    setEnergy(energy + 5);
    setNaquadah(naquadah + 2);
  }

  return (
    <div className="container">
      <img src="/logo.svg" alt="Stargate Logo" width={120} height={120} />
      <h1>Clone OGame Stargate</h1>
      <p>Tour: {turn}</p>
      <p>Metal: {metal} | Energie: {energy} | Naquadah: {naquadah}</p>
      <p>Flotte: {fleet}</p>
      <div className="buttons">
        <button onClick={buildMine}>Construire mine</button>
        <button onClick={buildShip}>Construire vaisseau</button>
        <button onClick={nextTurn}>Tour suivant</button>
      </div>
    </div>
  );
}
