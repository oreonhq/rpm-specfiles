%global source0_hash 4b02249c92228b03f4cc3c1d999cacf3fe52c16df53c6bf76fc6c1e2caa74318

Name: pipepanic
Version: 0.1.3
Release: 42%{?dist}
Summary: A pipe connecting game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.users.waitrose.com/~thunor/pipepanic/
Source0: http://www.users.waitrose.com/~thunor/pipepanic/dload/%{name}-%{version}-source.tar.gz
Source1: pipepanic.desktop
# Use standard Fedora CFLAGS to compile
Patch0: pipepanic-0.1.3-Makefile.patch
# Hans de Goede
# Set a window title and icon
Patch1: pipepanic-0.1.3-window-title.patch
# Miroslav Lichvar
# Fix wrong score with long pipes (BZ #847344)
Patch2: pipepanic-0.1.3-score.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: SDL-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
Requires: hicolor-icon-theme

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
# Install binary
mkdir -p %{buildroot}%{_bindir}
install -m 755 pipepanic %{buildroot}%{_bindir}

# Install data files
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 *.bmp %{buildroot}%{_datadir}/%{name}/

# Install window icon (needed by patch1)
convert PipepanicIcon32.png bmp3:- | \
  convert - -fill '#FF00FF' -opaque black -colors 256 \
    -compress none bmp3:icon.bmp
install -m 644 icon.bmp %{buildroot}%{_datadir}/%{name}/

# Install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m 644 PipepanicIcon16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 PipepanicIcon32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 PipepanicIcon48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m 644 PipepanicIcon64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

%files
%{_bindir}/pipepanic
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%doc AUTHORS ChangeLog README
%license COPYING COPYING-ARTWORK

%changelog
%autochangelog
