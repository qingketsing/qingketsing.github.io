// 音乐库配置文件
// 这个文件定义了可用的音乐资源，方便统一管理

export const musicLibrary = {
  // Yorushika 系列
  yorushika_8_31: {
    audioSrc: "/8_31.mp3",
    coverSrc: "/yorushika.jpg",
    title: "8/31",
    artist: "Yorushika"
  },
  
  yorushika_flower: {
    audioSrc: "/8_31.mp3", // 暂时使用同一个文件
    coverSrc: "/yorushika.jpg",
    title: "花と水飴, 最終電車",
    artist: "Yorushika"
  },

  zidaozidao: {
    audioSrc: "/zidaozidao.mp3", 
    coverSrc: "/zidaozidao.jpg",
    title: "ずっとずっとずっと",
    artist: "大橋トリオ"
  },

  stay_alive: {
    audioSrc: "/Stay_alive.mp3",
    coverSrc: "/Mitty.jpg",
    title: "Stay Alive",
    artist: "José González"
  },
};

// 获取音乐配置的辅助函数
export function getMusicConfig(musicKey) {
  return musicLibrary[musicKey] || null;
}
