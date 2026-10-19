%global source0_hash e27b2208823c5d53c3afe07206adf2bd7ff0cb7ae4db4ed3238230b02a044925
%global forgeurl https://github.com/groonga/groonga-normalizer-mysql
Version:        1.3.0
%forgemeta
Name:           groonga-normalizer-mysql
Release:        1%{?dist}
Summary:        A MySQL compatible normalizer plugin for Groonga
License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       groonga-libs
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  groonga-devel
BuildRequires:  msgpack-devel
BuildRequires:  ninja-build
# /oreon:deps
%description
Groonga-normalizer-mysql is a Groonga plugin. It provides MySQL compatible
normalizers and a custom normalizers to Groonga.

%package        devel
Summary:        Development files for groonga-normalizer-mysql
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides development files for groonga-normalizer-mysql.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
%cmake_build
%install
%cmake_install
rm -r %{buildroot}%{_datadir}/doc/groonga-normalizer-mysql
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n groonga-normalizer-mysql-devel -f %{oreon_filedir}/groonga-normalizer-mysql-devel.list

%changelog

%autochangelog
