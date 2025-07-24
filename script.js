const params = new URLSearchParams(window.location.search);
const playerId = params.get('player');

if (!playerId) {
  alert('Missing ?player=player001 in URL');
} else {
  fetch(`./player-id/${playerId}.json`)
    .then(res => {
      if (!res.ok) throw new Error(`Missing file: ${playerId}.json`);
      return res.json();
    })
    .then(data => {
      // Update UI
      document.getElementById('time').setAttribute('value', `Time: ${data.time}`);
      document.getElementById('target').setAttribute('value', `Target: ${data.target}`);
      document.getElementById('class').setAttribute('value', `Class: ${data.class}`);
      document.getElementById('dungeon').setAttribute('value', `Dungeon: ${data.dungeon}`);
      document.getElementById('mob').setAttribute('value', `Mob Killed: ${data.mob}`);
      document.getElementById('chest').setAttribute('value', `Chest: ${data.chest}`);
      document.getElementById('boss').setAttribute('value', `Boss Defeated: ${data.boss}`);
      document.getElementById('coins').setAttribute('value', `Coins Collected: ${data.coins}`);

      // Determine model
      let modelId = '';
      switch (data.class.toLowerCase()) {
        case 'mage': modelId = '#elfModel'; break;
        case 'duelist': modelId = '#dwarfModel'; break;
        case 'barbarian': modelId = '#orcModel'; break;
        default: modelId = '#dwarfModel';
      }

      const model = document.createElement('a-gltf-model');
      model.setAttribute('src', modelId);
      model.setAttribute('position', '0 -0.7 0.1');
      model.setAttribute('scale', '0.3 0.3 0.3');
      model.setAttribute('rotation', '0 180 0');
      document.querySelector('#model-anchor').appendChild(model);

      // Now show AR target content
      document.querySelector('[mindar-image-target]').setAttribute('visible', 'true');
    })
    .catch(err => {
      console.error('⚠️ Error loading player data:', err);
      alert('Failed to load player stats. Check the file or URL.');
    });
}