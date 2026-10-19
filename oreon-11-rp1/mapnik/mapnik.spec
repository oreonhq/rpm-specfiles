%global source3_hash 577722d9ec8f52b8369a989c2d4048c33be75cb90f9737f987c4f5cebdefabc2
%global source2_hash 96fc622a2891893ff37e8ff0235a65c9138223d199b5277717606d59e588b729
%global source1_hash 4b858c7d9cdc711832ddace213c32c773795e23ac9177e8e25e35a23fbec709f
%global source0_hash aadfe037a8fdf7524bca7d72594ed9783c7047b7a53c6cf2e767f6e802d53edd
%global vectortiledate 20250505
%global vectortilecommit 5a0cfbb6b909ae945f4a9e40777772a2b1c8fe9b
%global testcommit 5716a2794023035b64ced1143bf8a391dd9a0e02
%global visualcommit db003ccfe204725035e89e543e54cef764b1e3bb
%global vectortileshortcommit %(c=%{vectortilecommit}; echo ${c:0:7})
Name:      mapnik
Version:   4.3.1
Release:        1%{?dist}
Summary:        Free Toolkit for developing mapping applications
License:   LGPL-2.1-only
URL:       http://mapnik.org/
Source0:        https://github.com/mapnik/mapnik/releases/download/v%{version}/mapnik-v%{version}.tar.bz2
Source1:   https://github.com/mapnik/mapnik-vector-tile/archive/%{vectortilecommit}/mapnik-vector-tile-%{vectortilecommit}.tar.gz
Source2:   https://github.com/mapnik/test-data/archive/%{testcommit}/test-data-%{testcommit}.tar.gz
Source3:   https://github.com/mapnik/test-data-visual/archive/%{visualcommit}/test-data-visual-%{visualcommit}.tar.gz
Source4:   mapnik-data.license
Source5:   viewer.desktop
Patch:     mapnik-system-sparsehash.patch
Patch:     mapnik-system-catch.patch
Patch:     mapnik-visual-compare.patch
ExcludeArch: ppc ppc64 s390 s390x
Requires: dejavu-serif-fonts dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-lgc-serif-fonts dejavu-lgc-sans-fonts dejavu-lgc-sans-mono-fonts
Requires: proj
Provides: bundled(mapnik-vector-tile) = 3.0.1^%{vectortiledate}git%{vectortileshortcommit}
Provides: bundled(agg) = 2.4
Provides: bundled(boost)
%global __provides_exclude_from ^%{_libdir}/%{name}/input/.*$
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  boost-url
BuildRequires:  cairo-devel
BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  dejavu-sans-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel
BuildRequires:  geometry-hpp-devel
BuildRequires:  geometry-hpp-static
BuildRequires:  harfbuzz-devel
BuildRequires:  libavif-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libpq-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mapbox-variant-devel
BuildRequires:  mapbox-variant-static
BuildRequires:  pkgconfig
BuildRequires:  polylabel-devel
BuildRequires:  polylabel-static
BuildRequires:  postgis
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  proj-devel
BuildRequires:  protozero-devel
BuildRequires:  protozero-static
BuildRequires:  qt6-qtbase-devel
BuildRequires:  sparsehash-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
Mapnik is a Free Toolkit for developing mapping applications.
It's written in C++ and there are Python bindings to
facilitate fast-paced agile development. It can comfortably
be used for both desktop and web development, which was something
I wanted from the beginning.

Mapnik is about making beautiful maps. It uses the AGG library
and offers world class anti-aliasing rendering with subpixel
accuracy for geographic data. It is written from scratch in
modern C++ and doesn't suffer from design decisions made a decade
ago. When it comes to handling common software tasks such as memory
management, filesystem access, regular expressions, parsing and so
on, Mapnik doesn't re-invent the wheel, but utilises best of breed
industry standard libraries from boost.org 

%package devel
Summary: Mapnik is a Free toolkit for developing mapping applications
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: proj-devel libxml2-devel
Requires: boost-devel libicu-devel
Requires: libtiff-devel libjpeg-devel libpng-devel libwebp-devel
Requires: cairo-devel freetype-devel harfbuzz-devel
Requires: sparsehash-devel
Requires: geometry-hpp-devel
Requires: polylabel-devel
Requires: protozero-devel
Requires: mapbox-variant-devel
%description devel
Mapnik is a Free Toolkit for developing mapping applications.
It's written in C++ and there are Python bindings to
facilitate fast-paced agile development. It can comfortably
be used for both desktop and web development, which was something
I wanted from the beginning.

Mapnik is about making beautiful maps. It uses the AGG library
and offers world class anti-aliasing rendering with subpixel
accuracy for geographic data. It is written from scratch in
modern C++ and doesn't suffer from design decisions made a decade
ago. When it comes to handling common software tasks such as memory
management, filesystem access, regular expressions, parsing and so
on, Mapnik doesn't re-invent the wheel, but utilises best of breed
industry standard libraries from boost.org

%package static
Summary: Static libraries for the Mapnik spatial visualization library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description static
Static libraries for the Mapnik spatial visualization library.

%package utils
License:  GPL-2.0-or-later
Summary:  Utilities distributed with the Mapnik spatial visualization library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Miscellaneous utilities distributed with the Mapnik spatial visualization
library.

%package demo
Summary:  Demo utility and some sample data distributed with mapnik
License:  GPL-2.0-or-later AND LicenseRef-GeoGratis
Requires: %{name}-devel = %{version}-%{release}
Requires: python3-%{name}
%description demo
Demo application and sample vector datas distributed with the Mapnik
spatial visualization library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mapnik-v%{version} -a 1 -a 2 -a 3
%autopatch -p 1
rm -rf deps/mapbox/mapnik-vector-tile
mv mapnik-vector-tile-%{vectortilecommit} deps/mapbox/mapnik-vector-tile
cp -p %{SOURCE4} demo/data
rm -rf test/data test/data-visual
mv test-data-%{testcommit} test/data
mv test-data-visual-%{visualcommit} test/data-visual
find . -name '._*' -delete
iconv -f iso8859-1 -t utf-8 demo/data/COPYRIGHT.txt > COPYRIGHT.conv && mv -f COPYRIGHT.conv demo/data/COPYRIGHT.txt
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|' demo/simple-renderer/render.py
sed -i -e 's|+init=||' test/data/*_maps/*.xml
sed -i -e 's|+init=||' test/data-visual/styles/*.xml
rm -rf deps/mapnik/sparsehash deps/mapbox/geometry deps/mapbox/polylabel deps/mapbox/protozero deps/mapbox/variant

%build

%cmake \
  -DUSE_EXTERNAL_MAPBOX_GEOMETRY=ON \
  -DUSE_EXTERNAL_MAPBOX_POLYLABEL=ON \
  -DUSE_EXTERNAL_MAPBOX_PROTOZERO=ON \
  -DUSE_EXTERNAL_MAPBOX_VARIANT=ON \
  -DFONTS_INSTALL_DIR=share/fonts
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}/%{_bindir}/viewer.ini %{buildroot}/%{_datadir}/fonts
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE5}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PGTESTS_LOCALE="C.UTF-8" %postgresql_tests_run
createdb template_postgis
psql -c "CREATE EXTENSION postgis" template_postgis
%ctest
pushd redhat-linux-build/out
%ifarch aarch64 ppc64le
rm test/data-visual/styles/line-pattern-issue-2726.xml
%endif
./mapnik-test-visual -j %{_smp_build_ncpus} --output-dir ./visual-test-result
popd
%files -f %{oreon_filedir}/main.list
%files -n mapnik-devel -f %{oreon_filedir}/mapnik-devel.list
%files -n mapnik-static -f %{oreon_filedir}/mapnik-static.list
%files -n mapnik-utils -f %{oreon_filedir}/mapnik-utils.list
%files -n mapnik-demo -f %{oreon_filedir}/mapnik-demo.list

%changelog

%autochangelog
