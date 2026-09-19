%global source0_hash cbed266f396caf3a19db7b5e857a135ccf4f260451263a69b99680e09fe6b057

Name:           foobillard
Version:        3.0a
Release:        53%{?dist}

Summary:        OpenGL billard game

License:        GPL-2.0-only
URL:            http://foobillard.sunsite.dk/
# Based on http://foobillard.sunsite.dk/dnl/foobillard-3.0a.tar.gz
Source0:        foobillard-3.0a-hobbled.tar.bz2
Source1:        foobillard.desktop
Source2:        hobble-foobillard.sh
Patch0:         foobillard-3.0a-nonv.patch
Patch1:         foobillard-3.0a-no-fonts.patch
Patch2:		foobillard-3.0a-clothtex.patch
Patch3:         foobillard-configure-c99.patch
Patch4:         foobillard-c99.patch
Patch5:         pointer-types.patch
Requires:       dejavu-sans-fonts
BuildRequires:  gcc
BuildRequires:  SDL-devel ImageMagick alsa-lib-devel
BuildRequires:  freetype-devel libpng-devel perl-interpreter zlib-devel freeglut-devel
BuildRequires:  libGL-devel libGLU-devel libX11-devel libXaw-devel libXi-devel
BuildRequires:  make

%description
FooBillard is an attempt to create a free OpenGL-billard for Linux.
FooBillard is still under development but the main physics is implemented.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n foobillard-3.0a
%patch -P 0 -p1
%patch -P 1 -p1 -b .no-fonts
%patch -P 2 -p0 -b .clothtex
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p0

%build
iconv -f iso-8859-1 -t utf-8 < ChangeLog > _
mv _ ChangeLog
./configure --prefix=%{_prefix} --disable-nvidia --enable-SDL CFLAGS="${RPM_OPT_FLAGS} -DUSE_SOUND -std=gnu17" LDFLAGS="${RPM_LD_FLAGS}"
make %{?_smp_mflags}
convert -resize 48x48 -background transparent -gravity center -extent 48x48 data/foobillard.png foobillard.png
convert -resize 256x256 -background transparent -gravity center -extent 256x256 data/foobillard.png foobillard-256x256.png

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -pm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/applications/foobillard.desktop
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -pm 644 foobillard.6 $RPM_BUILD_ROOT%{_mandir}/man6
install -D -p -m 644 foobillard.png \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/foobillard.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 foobillard.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 foobillard-256x256.png \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

%files
%doc AUTHORS COPYING ChangeLog README TODO
%doc foobillardrc.example
%{_bindir}/foobillard
%{_datadir}/applications/foobillard.desktop
%{_datadir}/foobillard
%{_datadir}/pixmaps/foobillard.png
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_mandir}/man6/*

%changelog
%autochangelog
