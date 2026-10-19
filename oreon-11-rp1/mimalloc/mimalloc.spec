%global source0_hash 36e9b5bf1bb703567a0347491721ce2098000db8284dc55cd53d211452723cdb
%undefine __cmake_in_source_build
Name:           mimalloc
Version:        3.5.4
Release:        1%{?dist}
Summary:        A general purpose allocator with excellent performance
License:        MIT
URL:            https://github.com/microsoft/mimalloc
Source0:        https://github.com/microsoft/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
mimalloc (pronounced "me-malloc")
is a general purpose allocator with excellent performance characteristics.
Initially developed by Daan Leijen for the run-time systems.

%package devel
Summary:        Development environment for %name
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development package for mimalloc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# Remove unneded binary from sources
rm -rf bin

%build

%cmake \
    -DMI_BUILD_OBJECT=OFF \
    -DMI_OVERRIDE=OFF \
    -DMI_INSTALL_TOPLEVEL=ON \
    -DMI_BUILD_STATIC=OFF \
    -DMI_BUILD_TESTS=OFF \
    -DMI_NO_OPT_ARCH=ON \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mimalloc-devel -f %{oreon_filedir}/mimalloc-devel.list

%changelog

%autochangelog
