import './App.css';

function App() {
return (
    <div className="App">
    <header>
            <h1>柴田 優太</h1>
            <p>Learning data science and programming in university...</p>
            <p><a href="#About">About Me</a></p>
            <p><a href="#qualifications">Qualifications</a></p>
            <p><a href="#language">Programming language</a></p>
            <p><a href="#research">Research</a></p>
            <p><a href="#sns">SNS</a></p>
    </header>

    <main>
        <section id="About">
        <h2>About Me</h2>
        <nav>
            <ul>
                <p>名前:柴田 優太(しばた ゆうた)</p>
                <p>年齢:20</p>
                <p>誕生日:4月13日</p>
                <p>出身:東京</p>
                <p>所属:武蔵野大学データサイエンス学部データサイエンス学科</p>
            </ul>
        </nav>
        </section>

        <section id="qualifications">
        <h2>所持資格</h2>
        <nav>
            <ul>
                <p>普通自動車第一種運転免許</p>
                <p>実用英語技能検定 2級(最高スコア2158)</p>
                <p>珠算能力検定 準2級</p>
                <p>暗算検定 3級</p>
            </ul>
        </nav>
        </section>

        <section id="language">
        <h2>学習中のプログラミング言語</h2>
        <nav>
            <ul>
                <p>Python</p>
                <p>React</p>
                <p>HTML/CSS</p>
                <p>JavaScript</p>
            </ul>
        </nav>
        </section>

        <section id="research">
        <h2>現在の研究</h2>
        <nav>
            <ul>
            <p>研究タイトル:時系列データと仕事率を用いたパーソナル管理システムの実現</p>
            <p>研究の概要:<a href="https://docs.google.com/presentation/d/1yz86yZaYNgM084oPdGhHmK8QBR4xkimi5nGWIHKdaDI/edit?usp=sharing" target="_blank">Googleスライド</a></p>
            <p>研究のゴール:時空間データと仕事率を用いた仕事、健康管理を行い個々の作業パフォーマンス向上と健康維持の両立を図ること</p>
            <p>1年次の研究成果(PDFファイル):<a href="pdf.html" target="_blank">1年次成果発表会ポスター</a></p>
            </ul>
        </nav>
        </section>

        <section id="sns">
            <h2></h2>
        <nav>
            <ul>
            </ul>
        </nav>
        </section>
    </main>
    </div>
    );
};

export default App;

//以下メモ
//