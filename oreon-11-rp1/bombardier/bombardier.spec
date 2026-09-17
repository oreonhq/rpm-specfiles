%global source0_hash 4805a135a868cf2a8ce966e5cdb7e99b96137be8276cd9b01b7ed3b5f235efcf

Name: bombardier
Version: 0.8.4
Release: 3%{?dist}
Summary: The GNU Bombing utility

License: GPL-2.0-or-later        
URL: http://packages.debian.org/stable/source/bombardier
Source0: http://http.debian.net/debian/pool/main/b/bombardier/bombardier_%{version}.tar.xz
Source1: bombardier.desktop
Source2: bombardier-logo.png
Patch0: bombardier-height.patch
Patch1: bombardier-0.8.2-string-format.patch
Patch2: format.patch
BuildRequires: ncurses-devel, desktop-file-utils, gcc
BuildRequires: make
Requires: hicolor-icon-theme

%description
Fly an ncurses plane over an ncurses city, and try to level the buildings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn bombardier

%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
install -pD -m 755 bombardier %{buildroot}%{_bindir}/bombardier
install -pD -m 644 bombardier.6 %{buildroot}%{_mandir}/man6/bombardier.6

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install            \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%files
%{_bindir}/bombardier
%license COPYING
%doc README DEDICATION VERSION
%{_datadir}/applications/bombardier.desktop
%{_datadir}/icons/hicolor/32x32/apps/bombardier-logo.png
%{_mandir}/man6/bombardier.6.gz

%changelog
%autochangelog
