%global source0_hash d9dffa205a8ec4e7bf00d87183fd94d4a12f045fae04a6efd41d6557827233bc
Name:		quiterss
Version:	0.19.4
Release:        1%{?dist}
License:	GPL-3.0-only
Summary:        RSS/Atom aggregator
URL:		http://quiterss.org/
Source0:        https://github.com/QuiteRSS/quiterss/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qt5-linguist
BuildRequires:  qtsingleapplication-qt5-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
