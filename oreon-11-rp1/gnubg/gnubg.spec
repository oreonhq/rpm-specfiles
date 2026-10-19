%global source0_hash 6f7d969b13cfff786fba90ff8cc5e5d564b97f4f0aa69afe4f3838f18c445979
Name:          gnubg
License:       GPL-3.0-only
Summary:        A backgammon game and analyser
Epoch:         1
Version:       1.08.003
Release:        8%{?dist}
Source0:        https://ftp.gnu.org/gnu/gnubg/gnubg-release-%{version}-sources.tar.gz
Source1:       gnubg.desktop
Source2:       gnubg.png
URL:           https://www.gnu.org/software/gnubg/
Requires: dejavu-sans-fonts
Requires: dejavu-serif-fonts
# oreon:deps
BuildRequires:  atk-devel
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  freetype-devel
BuildRequires:  gettext-devel
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  gnuplot
BuildRequires:  gtk2-devel
BuildRequires:  info
BuildRequires:  libcanberra-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  netpbm-progs
BuildRequires:  pango-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  texinfo
# /oreon:deps
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
/bin/rm -f $RPM_BUILD_ROOT/usr/share/info/dir
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
