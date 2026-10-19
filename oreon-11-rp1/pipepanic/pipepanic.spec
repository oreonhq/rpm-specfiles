%global source0_hash 4b02249c92228b03f4cc3c1d999cacf3fe52c16df53c6bf76fc6c1e2caa74318
Name: pipepanic
Version: 0.1.3
Release:        42%{?dist}
Summary:        A pipe connecting game
License: GPL-2.0-or-later
URL: http://www.users.waitrose.com/~thunor/pipepanic/
Source0:        http://www.users.waitrose.com/~thunor/pipepanic/dload/%{name}-%{version}-source.tar.gz
Source1: pipepanic.desktop
Patch0: pipepanic-0.1.3-Makefile.patch
Patch1: pipepanic-0.1.3-window-title.patch
Patch2: pipepanic-0.1.3-score.patch
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Pipepanic is a pipe connecting game using libSDL. Connect as many 
different shaped pipes together as possible within the time given.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-source
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1

# Fix file encoding
iconv --from=ISO-8859-1 --to=UTF-8 COPYING-ARTWORK > COPYING-ARTWORK.conv 
mv COPYING-ARTWORK.conv COPYING-ARTWORK

# Fix DATADIR
sed -i 's:/opt/QtPalmtop/share/pipepanic/:%{_datadir}/%{name}/:' main.h

%build

%make_build \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{__global_ldflags}"
%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 pipepanic %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 *.bmp %{buildroot}%{_datadir}/%{name}/
convert PipepanicIcon32.png bmp3:- | \
  convert - -fill '#FF00FF' -opaque black -colors 256 \
    -compress none bmp3:icon.bmp
install -m 644 icon.bmp %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m 644 PipepanicIcon16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 PipepanicIcon32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 PipepanicIcon48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m 644 PipepanicIcon64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
