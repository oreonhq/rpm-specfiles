%global source0_hash dff32247e6fb7c1544ad9163a4a1cd2b048b71230c9cf5fc44e885dd9cb101e6

Name:           qascade
Version:        0.1
Release:        45%{?dist}
Summary:        Classic puzzle game

License:        GPL-2.0-or-later
URL:            http://www.bitsnpieces.org.uk/qascade/
Source0:        http://www.bitsnpieces.org.uk/qascade/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-dblsep.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt3-devel
BuildRequires:  desktop-file-utils

%description
Qascade is a port of the simple yet addictive and enjoyable puzzle
game that came with the Psion Revo PDA.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0

%build
[ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
qmake INSTALL_ROOT=$RPM_BUILD_ROOT qascade.pro
perl -pi -e 's|^(C(XX)?FLAGS\s*=.*)$|$1 \$(RPM_OPT_FLAGS)|g' Makefile
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
[ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%makeinstall
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  %{SOURCE1}
install -D -p -m 644 %{name}.hscr \
  $RPM_BUILD_ROOT%{_localstatedir}/lib/games/%{name}.hscr
install -D -p -m 644 blue.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/qascade.png

%files
%doc *.htm
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/qascade.png
%attr(0664,games,games) %config(noreplace) %{_localstatedir}/lib/games/%{name}*

%changelog
%autochangelog
