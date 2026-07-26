%global source0_hash e682229c2c914c7443122522851b771837391b0dd8033cf3e5d813e1f90caab2

Name:           lacewing
Version:        1.10
Release:        49%{?dist}
Summary:        Arcade-style shoot-em-up
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://users.olis.net.au/zel/
Source0:        http://users.olis.net.au/zel/lwsrc.zip
Source1:        http://users.olis.net.au/zel/lwdata.zip
Source2:        lacewing.desktop
Source3:        lacewing.png
Patch0:         lacewing.patch
Patch1:         lacewing-fullscreen.patch
Patch2:         lacewing-nicecpu.patch
Patch3:         lacewing-warn.patch
Patch4:         lacewing-format-security.patch
Patch5:         lacewing-rhbz1045111.patch
BuildRequires:  gcc
BuildRequires:  allegro-devel desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Arcade-style shoot-em-up where you can choose a type of ship and depending on
the type of ship can pickup a number of upgrades during the game.

Lacewing is an arcade-style shoot-em-up which plays a little bit like a cross
between Spacewar and Centipede. It has a decidedly retro style to it. It has
a single-player mode, and also co-operative and duel modes for two players
(split-screen).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
unzip -qqo %{SOURCE1}
%patch -P0 -p1 -z .unix
%patch -P1 -p1 -z .fullscreen
%patch -P2 -p1 -z .nicecpu
%patch -P3 -p1 -z .warn
%patch -P4 -p1
%patch -P5 -p1
sed -i 's/\r//' readme.txt licence.txt
chmod 644 readme.txt licence.txt

%build
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations"

%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor fedora            \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

%files
%doc readme.txt licence.txt
%{_bindir}/lacewing
%{_datadir}/lacewing
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-lacewing.desktop
%else
%{_datadir}/applications/lacewing.desktop
%endif
%{_datadir}/icons/hicolor/48x48/apps/lacewing.png

%changelog
%autochangelog
