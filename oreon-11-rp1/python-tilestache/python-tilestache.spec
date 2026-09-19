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

# Modify font search to find the system DejaVuSansMono.ttf - Not submitted upstream
Patch0:         %{name}-1.49.11-use-system-fonts.patch
# Don't install the bundled font or docs - Not submitted upstream
Patch1:         %{name}-1.49.11-unbundle-installs.patch
# Compatibility with Fedora's CGI - Not submitted upstream
Patch2:         %{name}-1.51.14-cgi-compat.patch
# Python 3 compatibility - Submitted upstream as TileStache/TileStache#345
Patch3:         %{name}-1.51.14-python3-compat.patch
# Non-standard python executable - Submitted upstream as TileStache/TileStache#359
Patch4:         %{name}-1.51.14-python3-executable.patch
# Bad escape in string literal - Submitted upstream as TileStache/TileStache#358
Patch5:         %{name}-1.51.14-escape-sequence.patch
# Support Shapely 2: Use shape instead of asShape from shapely.geometry
# Submitted upstream as TileStache/TileStache#375
Patch6:         %{name}-1.51.14-shapely2-compat.patch
# Replace assertEquals with assertEqual
# This deprecated unittest.TestCase alias was removed in Python 3.12.
# Submitted upstream as TileStache/TileStache#377
Patch7:         %{name}-1.51.14-assertEquals.patch

BuildArch:      noarch

%global _description\
TileStache is a Python-based server application that can serve up map tiles\
based on rendered geographic data. You might be familiar with TileCache, the\
venerable open source WMS server from MetaCarta. TileStache is similar, but we\
hope simpler and better-suited to the needs of designers and cartographers.

%description %_description

%package examples
Summary:        Example code for TileStache

%description examples
Example code for TileStache: A stylish alternative for caching your map tiles

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
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

%description -n python%{python3_pkgversion}-tilestache %_description

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

%check
NO_DATABASE=1 OFFLINE_TESTS=1 %pytest \
  --override-ini 'python_files=*_tests.py' \
  --ignore tests/vectiles_tests.py \
  tests

%files examples
%license LICENSE
%doc README.md
%{_datadir}/%{srcname}

%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc API.html CHANGELOG README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/tilestache-clean.py
%{_bindir}/tilestache-compose.py
%{_bindir}/tilestache-list.py
%{_bindir}/tilestache-render.py
%{_bindir}/tilestache-seed.py
%{_bindir}/tilestache-server.py
%{_mandir}/man1/tilestache-clean.1.gz
%{_mandir}/man1/tilestache-compose.1.gz
%{_mandir}/man1/tilestache-list.1.gz
%{_mandir}/man1/tilestache-render.1.gz
%{_mandir}/man1/tilestache-seed.1.gz
%{_mandir}/man1/tilestache-server.1.gz

%changelog
%autochangelog
