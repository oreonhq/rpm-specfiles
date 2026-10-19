%global source0_hash 785a47e5ef2b72b7bc9ed1aba87070707805703aee5101078fc1a10b3fffc6f5
%global pkgname tilestache
%global srcname TileStache
%global commit e96532bf59bf79c9991dcc06628f28b27bb19c08
Name:           python-%{pkgname}
Version:        1.51.14
Release:        25%{?dist}
Summary:        A stylish alternative for caching your map tiles
License:        BSD-3-Clause
URL:            http://tilestache.org
Source0:        https://github.com/%{srcname}/%{srcname}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
Patch0:         %{name}-1.49.11-use-system-fonts.patch
Patch1:         %{name}-1.49.11-unbundle-installs.patch
Patch2:         %{name}-1.51.14-cgi-compat.patch
Patch3:         %{name}-1.51.14-python3-compat.patch
Patch4:         %{name}-1.51.14-python3-executable.patch
Patch5:         %{name}-1.51.14-escape-sequence.patch
Patch6:         %{name}-1.51.14-shapely2-compat.patch
Patch7:         %{name}-1.51.14-assertEquals.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-gdal
BuildRequires:  python3-memcached
BuildRequires:  python3-modestmaps
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-shapely
BuildRequires:  python3-werkzeug
# /oreon:deps
%description

%package examples
Summary:        Example code for TileStache
%description examples
Example code for TileStache: A stylish alternative for caching your map tiles

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        A stylish alternative for caching your map tiles
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-gdal
BuildRequires:  python%{python3_pkgversion}-memcached
BuildRequires:  python%{python3_pkgversion}-modestmaps >= 1.3.0
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-shapely
BuildRequires:  python%{python3_pkgversion}-werkzeug
Requires:       font(dejavusansmono)
Conflicts:      python2-%{pkgname} < %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-imaging
Requires:       python%{python3_pkgversion}-modestmaps >= 1.3.0
Requires:       python%{python3_pkgversion}-simplejson
Requires:       python%{python3_pkgversion}-werkzeug
%endif # __pythondist_requires
%description -n python%{python3_pkgversion}-tilestache

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{commit}

# Remove shebang from a script
sed -i '1{\@^#!/usr/bin/env python@d}' %{srcname}/Goodies/Caches/GoogleCloud.py

# Add shebang to a script
sed -i '1i #!%{_bindir}/bash' examples/zoom_example/run_server.sh

sed -i '1{s@^#!/usr/bin/env python@#!%{__python3}@}' examples/geotiff/server.py

%build

%py3_build
%install
%py3_install
install -d %{buildroot}%{_mandir}/man1
install -p -m0644 man/tilestache-clean.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-compose.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-list.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-render.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-seed.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-server.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_datadir}/%{srcname}
cp -a examples %{buildroot}%{_datadir}/%{srcname}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

NO_DATABASE=1 OFFLINE_TESTS=1 %pytest \
  --override-ini 'python_files=*_tests.py' \
  --ignore tests/vectiles_tests.py \
  tests
%files -f %{oreon_filedir}/main.list
%files -n python-tilestache-examples -f %{oreon_filedir}/python-tilestache-examples.list
%files -n python3-tilestache -f %{oreon_filedir}/python3-tilestache.list

%changelog

%autochangelog
