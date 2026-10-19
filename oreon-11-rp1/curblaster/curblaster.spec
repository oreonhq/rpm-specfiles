%global source0_hash 4fd7e4d80c119cfd3af92e3d8892519a1f31d998a812d8019bdacb84a9b130ef
Name: curblaster
Version:  1.15
Release:        1%{?dist}
Summary:        Sidescrolling shooter, carry the pods through the gate
License: GPL-3.0-or-later
URL: https://codeberg.org/gwync/curblaster
Source0:        https://codeberg.org/gwync/curblaster/archive/%{version}.tar.gz
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL2_mixer-devel
BuildRequires:  cppcheck
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Grab pods and drop them in the gate, while fighting enemies in your way.
Multiple weapons available.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn curblaster

%build

%configure
make %{?_smp_mflags}
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/appdata
install -m 644 curblaster.appdata.xml %{buildroot}%{_datadir}/appdata/
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
  curblaster.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 curblaster-logo.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
