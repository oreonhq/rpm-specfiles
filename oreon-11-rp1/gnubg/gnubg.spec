%global source0_hash 6f7d969b13cfff786fba90ff8cc5e5d564b97f4f0aa69afe4f3838f18c445979

Name:          gnubg
License:       GPL-3.0-only
Summary:       A backgammon game and analyser
Epoch:         1
Version:       1.08.003
Release:       8%{?dist}
Source0:       https://ftp.gnu.org/gnu/gnubg/gnubg-release-%{version}-sources.tar.gz
Source1:       gnubg.desktop
Source2:       gnubg.png

URL:           https://www.gnu.org/software/gnubg/
BuildRequires: libcanberra-devel
BuildRequires: sqlite-devel
BuildRequires: gmp-devel
BuildRequires: gtk2-devel
BuildRequires: gettext-devel
BuildRequires: automake
BuildRequires: bison
BuildRequires: libtool
BuildRequires: texinfo
BuildRequires: netpbm-progs
BuildRequires: gnuplot
BuildRequires: ghostscript
BuildRequires: info
BuildRequires: desktop-file-utils
BuildRequires: cairo-devel
BuildRequires: atk-devel
BuildRequires: pango-devel
BuildRequires: libpng-devel
BuildRequires: readline-devel
BuildRequires: freetype-devel
BuildRequires: flex
BuildRequires: make
#BuildRequires: gtkglext-devel
#BuildRequires: mesa-libGLU-devel
Requires: dejavu-sans-fonts
Requires: dejavu-serif-fonts

%description
GNU Backgammon is software for playing and analysing backgammon
positions, games and matches. It's based on a neural network. Although it
already plays at a very high level, it's still work in progress. You may
play GNU Backgammon using the command line or a graphical interface

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

/usr/bin/iconv -f ISO-8859-1 -t UTF8 ChangeLog > ChangeLog.tmp 
/bin/mv ChangeLog.tmp ChangeLog

%build
%ifarch x86_64
SSE=sse2
%else
SSE=no
%endif

%configure --with-python=no --enable-simd=$SSE --with-gtk --with-board3d=no
%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnubg
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnubg/fonts/*.ttf
ln -s ../../fonts/dejavu-sans-fonts/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/gnubg/fonts/Vera.ttf
ln -s ../../fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/gnubg/fonts/VeraBd.ttf 
ln -s ../../fonts/dejavu-serif-fonts/DejaVuSerif-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/gnubg/fonts/VeraSeBd.ttf 
install -Dpm 644 gnubg.weights $RPM_BUILD_ROOT%{_datadir}/gnubg/gnubg.weights

cp -rp textures* $RPM_BUILD_ROOT%{_datadir}/gnubg/
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnubg/textures/CVS
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnubg/textures/.cvsignore
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/gnubg/

%find_lang gnubg

# remove /usr/share/info/dir
/bin/rm -f $RPM_BUILD_ROOT/usr/share/info/dir

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

%files -f gnubg.lang
%license COPYING
%doc AUTHORS README ChangeLog doc/images doc/*.html doc/*.pdf
%{_bindir}/bearoffdump
%{_bindir}/gnubg
%{_bindir}/makebearoff
%{_bindir}/makehyper
%{_bindir}/makeweights
%dir %{_datadir}/gnubg
%{_datadir}/gnubg/met
%{_datadir}/gnubg/boards.xml
%{_datadir}/gnubg/gnubg_os0.bd
%{_datadir}/gnubg/gnubg.weights
%{_datadir}/gnubg/sounds
%{_datadir}/gnubg/textures.txt
%{_datadir}/gnubg/textures
%{_mandir}/man6/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/gnubg/pixmaps/gnubg-big.png
%{_datadir}/icons/hicolor/16x16/apps/gnubg.png
%{_datadir}/icons/hicolor/22x22/apps/gnubg.png
%{_datadir}/icons/hicolor/24x24/apps/gnubg.png
%{_datadir}/icons/hicolor/48x48/apps/gnubg.png
%dir %{_datadir}/gnubg/fonts
%{_datadir}/gnubg/fonts/*
%{_datadir}/gnubg/gnubg.gtkrc
%{_datadir}/gnubg/gnubg.wd
%{_datadir}/gnubg/scripts/
%{_datadir}/gnubg/flags/
%{_datadir}/gnubg/gnubg.sql
%{_datadir}/gnubg/gnubg_ts0.bd
%{_datadir}/gnubg/gnubg.css
%{_datadir}/gnubg/Shaders/

%changelog
%autochangelog
