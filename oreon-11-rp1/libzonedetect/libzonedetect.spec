%global source3_hash 27b22e6e82672d07774562a09055a2e9d53f08e020b80720f9ea92f005809677
%global source2_hash 3f1596b05b4a19bd97f3a54731497cffbb4dbed4cda494084e73dd6dd3d37264
%global source0_hash 07a02e02b353948064a5e97e7296b2146fc0f6151af305a3521e1937885695aa
%global commit 082fa6b14815340d0f0d9e23b1ded318ba77c82c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global tz_ver 2024b
Name:          libzonedetect
Version:       0~git%{shortcommit}
Release:        1%{?dist}
Summary:        Find the timezone for a given latitude and longitude
License:       BSD-3-Clause AND MIT AND ODbL-1.0
URL:           https://github.com/BertoldVdb/ZoneDetect
Source0:        https://github.com/BertoldVdb/ZoneDetect/archive/%{commit}/ZoneDetect-%{shortcommit}.tar.gz
Source1:       CMakeLists.txt
Source2:       https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries_lakes.zip
Source3:       https://github.com/evansiroky/timezone-boundary-builder/releases/download/%{tz_ver}/timezones-with-oceans.shapefile.zip
Source4:       README.data
Patch1:        ZoneDetect_builddb.patch
Patch2:        ZoneDetect_demo.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  shapelib-devel
# /oreon:deps
%description
Find the timezone for a given latitude and longitude.

%package devel
Summary:       Development files for %{name}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
%description -n mingw64-%{name}
MinGW Windows %{name} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ZoneDetect-%{commit}
cp -a %{SOURCE1} .

# Prepare for DB build
mkdir -p database/builder/{naturalearth,timezone}
cp -a %{SOURCE2} database/builder/naturalearth/ne.zip
cp -a %{SOURCE3} database/builder/timezone/tz.zip
find database/builder/

%build

(cd database/builder/ && ./makedb.sh)
%cmake
%cmake_build
%mingw_cmake
%mingw_make_build
%install
%cmake_install
%mingw_make_install
mkdir -p %{buildroot}%{_datadir}/ZoneDetect/
cp -a database/builder/out_v1/* %{buildroot}%{_datadir}/ZoneDetect/
cp -a %{SOURCE4} %{buildroot}%{_datadir}/ZoneDetect/
%mingw_debug_install_post
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libzonedetect-devel -f %{oreon_filedir}/libzonedetect-devel.list
%files -n mingw32-libzonedetect -f %{oreon_filedir}/mingw32-libzonedetect.list
%files -n mingw64-libzonedetect -f %{oreon_filedir}/mingw64-libzonedetect.list

%changelog

%autochangelog
