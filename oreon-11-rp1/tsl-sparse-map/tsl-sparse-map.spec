%global source0_hash b603a24f596f95a06ec1d437f4cb928c2647cf9bc73b751ac6fb82deb7863d98
%global debug_package %{nil}
%global srcname sparse-map
Name:           tsl-%{srcname}
Version:        0.7.0
Release:        1%{?dist}
Summary:        C++ implementation of a memory efficient hash map and hash set
License:        MIT
URL:            https://github.com/Tessil/%{srcname}
Source0:        https://github.com/Tessil/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sed
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
%description    devel

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Warnings shouldn't break the build
sed -i 's/-Werror//' tests/CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd tests
%cmake
%cmake_build
./%{_vpath_builddir}/tsl_sparse_map_tests
%files -f %{oreon_filedir}/main.list
%files -n tsl-sparse-map-devel -f %{oreon_filedir}/tsl-sparse-map-devel.list

%changelog

%autochangelog
