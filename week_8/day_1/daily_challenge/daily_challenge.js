class Video {
    constructor(title, uploader, time){
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    watch(){
        console.log(`${this.uploader} watched all ${this.time} min of ${this.title}`);
    }
}

const video = new Video('Kung fu panda','Bob', 120);
video.watch()

const film = new Video('Ohio', 'Marley', 300);
film.watch()

const movies = [
    ['Star Wars', 'Dark vader', 180],
    ['Deadpool', 'Reynold', 160],
    ['Wolverine', 'Analogan', 120],
    ['Venom', 'Eminem', 210],
    ['Megalodon', 'Gore', 240]
];

const flick = [];

for(const video of movies){

    const [title, uploader, time] = video;
    const video2 = new Video(title, uploader, time);
    flick.push(video2);
}

for(const video of flick){
    video.watch()
}