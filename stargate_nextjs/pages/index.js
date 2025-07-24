import { useState } from 'react';

export default function Home() {
  const [metal, setMetal] = useState(100);
  const [energy, setEnergy] = useState(100);
  const [naquadah, setNaquadah] = useState(50);
  const [crystal, setCrystal] = useState(50);
  const [fleet, setFleet] = useState(0);
  const [defense, setDefense] = useState(0);
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

  function buildTurret() {
    const costMetal = 40;
    const costCrystal = 20;
    if (metal >= costMetal && crystal >= costCrystal) {
      setMetal(metal - costMetal);
      setCrystal(crystal - costCrystal);
      setDefense(defense + 1);
    } else {
      alert('Ressources insuffisantes');
    }
  }

  function nextTurn() {
    setTurn(turn + 1);
    setMetal(metal + 10);
    setEnergy(energy + 5);
    setNaquadah(naquadah + 2);
    setCrystal(crystal + 3);
    if (Math.random() < 0.3) {
      if (defense + fleet > 0) {
        alert("Une attaque ennemie a été repoussée !");
      } else {
        const loss = Math.min(metal, 20);
        setMetal(metal - loss);
        alert(`Vous subissez une attaque et perdez ${loss} metal`);
      }
    }
  }

  return (
    <div style={{ fontFamily: 'sans-serif', padding: '2rem' }}>
      <h1>Clone OGame Stargate</h1>
      <p>Tour: {turn}</p>
      <p>Metal: {metal} | Energie: {energy} | Naquadah: {naquadah} | Cristal: {crystal}</p>
      <p>Flotte: {fleet} | Défense: {defense}</p>
      <button onClick={buildMine}>Construire mine</button>
      <button onClick={buildShip} style={{ marginLeft: '0.5rem' }}>
        Construire vaisseau
      </button>
      <button onClick={buildTurret} style={{ marginLeft: '0.5rem' }}>
        Construire tourelle
      </button>
      <button onClick={nextTurn} style={{ marginLeft: '0.5rem' }}>
        Tour suivant
      </button>
    </div>
  );
}
