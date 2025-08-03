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

  // 可以继续添加更多音乐
  // peaceful_ambient: {
  //   audioSrc: "/peaceful-ambient.mp3",
  //   coverSrc: "/peaceful-cover.jpg",
  //   title: "Peaceful Ambient",
  //   artist: "Nature Sounds"
  // }
};

// 获取音乐配置的辅助函数
export function getMusicConfig(musicKey) {
  return musicLibrary[musicKey] || null;
}
