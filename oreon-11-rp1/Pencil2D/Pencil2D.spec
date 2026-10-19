%global source0_hash 22af8bf304cd18ae5d7a84e66d80ea2a21a53963476ffabb60d1d5f37f091a0c
Name:           Pencil2D
Version:        0.7.2
Release:        1%{?dist}
Summary:        Create traditional hand-drawn animation (cartoon)
Summary(ca):    Crear animacions tradicionals fetes a mà (dibuixos animats)
Summary(en):    Create traditional hand-drawn animation (cartoon)
Summary(es):    Crear animaciones (cartoons) de manera tradicional
Summary(fr):    Créer une animation traditionnelle (dessin animé) à la main
Summary(it):    Creare animazioni tradizionali disegnate a mano (cartoni animati)
Summary(pt_BR): Criar animações tradicionais feitas a mão (desenhos animados)
Summary(pt):    Criar animações tradicionais feitas a mão (desenhos animados)
License:        GPL-2.0-only AND BSD-3-Clause AND GPL-2.0-or-later
SourceLicense:  %{shrink:
                %{license} AND
                BSL-1.0 AND
                CC0-1.0 AND
                MIT AND
                Unlicense
                }
URL:            https://www.pencil2d.org
%global forgeurl https://github.com/pencil2d/pencil
Source0:        %{forgeurl}/archive/v%{version}/pencil-%{version}.tar.gz
Patch:          %{forgeurl}/pull/1914.patch
Patch:          0001-Downstream-only-Hide-Check-for-Updates-in-the-Help-m.patch
ExcludeArch:    %{ix86}
Requires:       /usr/bin/ffmpeg
Requires:       qt6-qtsvg
Requires:       hicolor-icon-theme
%global app_id org.pencil2d.Pencil2D
# oreon:deps
BuildRequires:  /usr/bin/ffmpeg
BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(catch2)
BuildRequires:  pkgconfig(miniz)
BuildRequires:  qt6-linguist
# /oreon:deps
%description
Pencil2D is an animation/drawing software for Mac OS X, Windows, and Linux. It
lets you create traditional hand-drawn animation (cartoon) using both bitmap
and vector graphics.

%description -l ar
بنسل2دي هو برنامج رسوم متحركة متوفر لـ ماك أو أس أكس و ويندوز و لينكس. يسمح لك
بعمل رسوم متحركة متحركة مرسومة باليد برسوم نقطية أو متجهة.

# %%description -l bg
# (no upstream translation)

%description -l ca
Pencil2D es un software d’animació/dibuix per a Mac OS X, Windows i Linux.
Permet crear animacions tradicionals fetes a mà (dibuixos animats) utilitzant
gràfics rasteritzats i/o vectorials.

%description -l cs
Pencil2D je animační/kreslicí program pro operační systémy Mac OS X, Windows a
Linux. Dovolí vám tvořit tradiční ručně kreslenou animaci pomocí bitmapové i
vektorové grafiky

%description -l da
Pencil2D er et animations/tegne software for Mac OS X, Windows og Linux. Det
lader dig skabe traditionel håndtegnet animation (tegnefilm) med både bitmap og
vektor grafik.

%description -l de
Pencil2D ist eine Animations-/Zeichensoftware für Mac OS X, Windows und Linux.
Sie eignet sich zum Schaffen von traditioneller handgezeichneter Animation
(Zeichentrick) sowohl mit Raster- als auch mit Vektorgrafik.

%description -l el
Pencil2D είναι ένα λογισμικό κινουμένων σχεδίων/ζωγραφικής για Mac OS X,
Windows, και Linux. Δίνει τη δυνατότητα δημιουργίας παραδοσιακών, ζωγραφισμένων
στο χέρι κινούμενων σχεδίων (καρτούν) χρησιμοποιώντας bitmap και διανυσματική
γραφιστική.

%description -l en
Pencil2D is an animation/drawing software for Mac OS X, Windows, and Linux. It
lets you create traditional hand-drawn animation (cartoon) using both bitmap
and vector graphics.

%description -l es
Pencil2D es un programa de animación/dibujo para Mac OS X, Windows y Linux. Te
permite crear animaciones (cartoons) de manera tradicional y cuenta con mapa de
bits y gráficos vectoriales.

# %%description -l et
# (no upstream translation)

# %%description -l fa
# (no upstream translation)

%description -l fr
Pencil2D est un logiciel d’animation/dessin pour Mac OS X, Windows et Linux. Il
vous permet de créer une animation traditionnelle (dessin animé) à la main en
utilisant à la fois des images matricielles et des graphiques vectoriels.

%description -l he
Pencil2D היא תוכנת ציור והנפשה עבור Mac OS X, Windows ו-Linux. היא מאפשרת לך
ליצור הנפשות בסגנון מסורתי מצוייר ביד (cartoon) תוך שימוש בכלי מפת ביטים וכלים
וקטוריים.

%description -l hu_HU
A Pencil2D egy animáció készítő/rajzoló szoftver Mac OS X, Windows és Linux
rendszerekre. Hagyományos, kézzel rajzolt animációk készítésére alkalmas
bitképek és vektorgrafika használatával.

# %%description -l id
# (no upstream translation)

%description -l it
Pencil2D è un software di animazione/disegno per Mac OS X, Windows e Linux. Ti
consente di creare animazioni tradizionali disegnate a mano (cartoni animati)
utilizzando sia grafica bitmap che vettoriale.

%description -l ja
Pencil2DはMac OS X, Windows, and Linuxに対応したアニメーション及びドローイング
ソフトです。本ソフトウェアのベクター・ビットマップ両方の描画機能を使用して、一
般的なコマ送りアニメーションを作成できます。

%description -l kab
Pencil2D d aseɣẓan n usmussu akked usuneɣ i Mac OS X, Windows, akked Linux. Ad
k-yeǧǧ ad d-tesnulfuḍ unuɣen yettemwwiwilen ara tsunɣeḍ s ufus s useqdec n
wudlifen n bitmap akked wudlifen imawayen.

%description -l ko
Pencil2D는 맥 OS X, 윈도우, 리눅스에서 지원되는 애니메이션/그림그리기
소프트웨어입니다. 비트맵과 벡터 모두를 사용하여 손 그림 애니메이션(만화)를 만들
수 있게 해줍니다.

# %%description -l nb
# (no upstream translation)

# %%description -l nl_NL
# (no upstream translation)

%description -l pl
Pencil2D to program do animacji/rysowania dla Mac OS X, Windows, i Linux. Ono
pozwala ci tworzyć tradycyjne ręcznie rysowane animacje (kreskówki) używając
bitmap i grafiki wektorowej.

%description -l pt_BR
Pencil2D é um programa de animação/desenho para Mac OS X, Windows e Linux.
Permite criar animações tradicionais feitas a mão (desenhos animados)
utilizando gráficos bitmaps e vetoriais.

%description -l pt
Pencil2D é um programa de animação/desenho para Mac OS X, Windows e Linux.
Permite criar animações tradicionais feitas a mão (desenhos animados)
utilizando gráficos bitmaps e vetoriais.

%description -l ru
Pencil2D — программа для рисования и анимации, которая работает в Mac OS X,
Windows и Linux. С помощью неё можно создавать традиционную рисованную анимацию
(мультфильмы) на основе как растровой, так и векторной графики.

%description -l sl
Svinčnik2D je program za animacijo/risanje v Mac OS X, Windows in Linux-u. Z
njim lahko ustvarite tradicionalno ročno risano animacijo (risanko) s pomočjo
bitne in vektorske grafike

%description -l sv
Pencil2D är ett animations- / ritprogram för Mac OSX, Windows och Linux. Det
låter dig skapa traditionellt handritad animering (tecknat) med både bitmapp
och vektorgrafik.

%description -l tr
Pencil2D, Mac OS X, Windows ve Linux için bir animasyon/çizim yazılımıdır. Hem
bitmap hem de vektör grafikleri kullanarak geleneksel elle çizilmiş animasyon
(çizgi film) oluşturmanıza olanak tanır.

# %%description -l vi
# (no upstream translation)

%description -l yue
Pencil2D là một phần mềm hoạt hình / vẽ cho Mac OS X, Windows và Linux. Nó cho
phép bạn tạo hoạt ảnh vẽ tay truyền thống (phim hoạt hình) bằng cách sử dụng cả
đồ họa bitmap và đồ họa vector.

%description -l zh_CN
Pencil2D是适用于Mac OS X，Windows和Linux的动画/绘图软件。它允许您使用位图和矢量
图形创建传统的手绘动画（卡通）。

%description -l zh_TW
Pencil2D是适用于Mac OS X，Windows和Linux的动画/绘图软件。它允许您使用位图和矢量
图形创建传统的手绘动画（卡通）。

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pencil-%{version} -p1

# Unbundle miniz
rm -v core_lib/src/miniz.h core_lib/src/miniz.cpp
sed -r -i '/\bminiz\.(h|cpp)/d' core_lib/core_lib.pro
echo "LIBS_PRIVATE += $(pkgconf --libs miniz)" | tee -a */*.pro >/dev/null
echo "INCLUDEPATH += $(pkgconf --variable=includedir miniz)" | tee -a */*.pro >/dev/null

# Unbundle catch2, using version 3.x
# https://catch2-temp.readthedocs.io/en/latest/migrate-v2-to-v3.html
echo '#include <catch2/catch_all.hpp>' > tests/src/catch.hpp
echo "LIBS += $(pkgconf --libs catch2)" >> tests/tests.pro

%conf
# We want the compiled-in version information to describe this as a release
# build to the user. We could set DEFINES+=PENCIL2D_RELEASE, but that would set
# QT_NO_DEBUG_OUTPUT; we would rather preserve that to help with debugging, as
# it does no harm except for a slight impact on performance. Instead, we define
# PENCIL2D_RELEASE_BUILD directly. See common.pri for details.
%{qmake_qt6} \
    PREFIX='%{_prefix}' \
    DEFINES+=PENCIL2D_RELEASE_BUILD \
    VERSION='%{version}'

%build

%make_build
QT_QPA_PLATFORM=offscreen help2man --no-info --output=pencil2d.1 ./app/pencil2d
%install
%make_install INSTALL_ROOT='%{buildroot}'
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 pencil2d.1
%oreon_autofiles main

%check

desktop-file-validate '%{buildroot}%{_datadir}/applications/%{app_id}.desktop'
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
appstreamcli validate --no-net --explain \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
QT_QPA_PLATFORM=offscreen ./tests/tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
