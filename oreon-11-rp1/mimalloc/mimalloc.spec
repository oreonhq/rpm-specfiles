%global source0_hash ac5ba94172b60823215a22b87ae923c5b05ef0cdd9047df2a832c16da02a6447

%undefine __cmake_in_source_build

Name:           mimalloc
Version:        2.2.3
Release:        4%{?dist}
Summary:        A general purpose allocator with excellent performance

License:        MIT
URL:            https://github.com/microsoft/mimalloc
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix ppc64le build
# Patch0:         3966953b7f0f11d2ec33097c5da4356d5b7db7e8.patch
# Patch1:         cc3c14f2ed374f908e60a3bf29c1dff84fc8cfc2.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

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


%files
%license LICENSE
%doc readme.md
%{_libdir}/lib%{name}.so.2*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*


%changelog
%autochangelog
