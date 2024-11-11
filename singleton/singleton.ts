class Singleton {
  private static instance: Singleton;
  isLonely: boolean;


  private constructor() {
    this.isLonely = true;
  }

  public static getInstance(): Singleton {
    if (Singleton.instance) {
      return Singleton.instance;
    }

    return Singleton.instance = new Singleton();
  }
}

console.log(Singleton.getInstance())