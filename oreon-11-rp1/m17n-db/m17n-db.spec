%global source1_hash 350b47b993f5d57deedc2e5c85a1cec02ea0be3b8d78c3ec1f2539002aabbdc0
%global source0_hash 783e1a9440be2c9221cdded9dd9b276a8c51d34559feaf62017aedb5dc43da41
Name:       m17n-db
Summary:        Multilingualization datafiles for m17n-lib
Version:    1.8.14
Release:        1%{?dist}
License:    LGPL-2.1-or-later
URL:        http://www.nongnu.org/m17n
Source0:        https://download-mirror.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
Source1:    https://raw.githubusercontent.com/gnuman/m17n-inglish-mims/master/minglish/minglish.mim
BuildArch:  noarch
Obsoletes:  m17n-contrib < 1.1.14-4.fc20
Provides:   m17n-contrib = 1.1.14-4.fc20
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glibc-locale-source
BuildRequires:  make
# /oreon:deps
%description
This package contains multilingualization (m17n) datafiles for m17n-lib
which describe input maps, encoding maps, OpenType font data and
font layout text rendering for languages.

%package extras
Summary:  Extra m17n-db files
Requires: %{name} = %{version}-%{release}
Obsoletes:  m17n-contrib-extras < 1.1.14-4.fc20
Provides:   m17n-contrib-extras = 1.1.14-4.fc20
%description extras
m17n-db extra files for input maps that are less used.

%package devel
Summary:  Development files for m17n-db
Requires: %{name} = %{version}-%{release}
%description devel
m17n-db development files

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -N -n m17n-db-%{version}

%autopatch -p0

%build

%configure
%{make_build}
%install
%{make_install}
rm %{buildroot}%{_datadir}/m17n/ispell.mim
/usr/bin/install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/m17n
%find_lang %name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n m17n-db-extras -f %{oreon_filedir}/m17n-db-extras.list
%files -n m17n-db-devel -f %{oreon_filedir}/m17n-db-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.11-1
- Import
