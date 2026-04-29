// Script global pour l'application 
console.log('Application collecte chargee')
// fontion utilitaire pour formater les nombres
function formaterNombre(nombre, decimales = 2) {
    return parseFloat(nombre).toFixed(decimales);
}

// Fonction pour afficher les notifications 
function afficherNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 3000);
}
// Gestion du theme (clair/sombre)
function basculerTheme() {
    document.body.classList.toggle('theme-sombre');
    const theme = Document.body.classList.contains('theme-sombre') ? 'sombre' : 'clair';
    localStorage.setItem('theme', theme);
}
//Chargement du theme sauvegarde
const themesauvegarde = localStorage.getItem('theme');
if (themesauvegarde === 'sombre') {
    document.body.classList.add('theme-sombre');
}
