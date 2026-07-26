%global source0_hash d9dffa205a8ec4e7bf00d87183fd94d4a12f045fae04a6efd41d6557827233bc

Name:		quiterss
Version:	0.19.4
Release:	16%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
Summary:	RSS/Atom aggregator
URL:		http://quiterss.org/
Source0:	https://github.com/QuiteRSS/quiterss/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# sqlite-devel
BuildRequires: make
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qtsingleapplication-qt5-devel
# qt5-qtwebkit-devel
BuildRequires:  pkgconfig(Qt5WebKit)
# qt5-qtmultimedia-devel
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  qt5-linguist
BuildRequires:	desktop-file-utils

%description
Qt-based RSS/Atom aggregator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# be asure
rm -rf 3rdparty/{qtsingleapplication,sqlite}

%build
%{qmake_qt5} PREFIX=%{_prefix} SYSTEMQTSA=True

%make_build release

%install
make install INSTALL_ROOT=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%doc AUTHORS CHANGELOG README.md
%license COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/sound/
%{_datadir}/%{name}/style/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
