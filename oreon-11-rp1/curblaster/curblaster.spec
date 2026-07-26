%global source0_hash d9ac779633f1a0cd4057da300040397923e1075609671fb5da3c3aaae35c9968

Name: curblaster
Version:  1.15
Release:  4%{?dist}
Summary: Sidescrolling shooter, carry the pods through the gate

License: GPL-3.0-or-later
URL: https://codeberg.org/gwync/curblaster
Source0: https://codeberg.org/gwync/curblaster/archive/%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires: ncurses-devel, desktop-file-utils, SDL2_mixer-devel, cppcheck
BuildRequires: make
Requires: hicolor-icon-theme

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

%check
make check

%files
%license COPYING
%{_bindir}/curblaster
%doc ChangeLog README
%{_datadir}/applications/curblaster.desktop
%{_datadir}/icons/hicolor/32x32/apps/curblaster-logo.png
%{_datadir}/curblaster/
%{_mandir}/man6/curblaster.6.gz
%{_datadir}/appdata/curblaster.appdata.xml

%changelog
%autochangelog
