%global source0_hash 6be27e0b3a4907f0cd3cfadec255ee1b925569e1bd06e67a4d2f4267299b69c4

%global commit ca1bf4b810e2d188d04cb6286f957008ee1b7681
%global short_commit %(c=%{commit}; echo ${c:0:7})	
%global date 20190529

Name: crossguid2
Version: 0.2.2
Release: 23.%{date}git%{short_commit}%{?dist}
Summary: Lightweight cross platform C++ GUID/UUID library
License: MIT
URL: https://github.com/graeme-hill/crossguid/
Source0: %{url}/archive/%{commit}/crossguid-%{commit}.tar.gz

# Fix library and directory names
Patch0: %{name}-fix_name.patch
Patch1: %{name}-fix_GCC13.patch

BuildRequires: gcc-c++, cmake
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: marshalparser

%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and has a generic class for
parsing, stringifying, and comparing IDs.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libuuid-devel%{?_isa}
Requires: cmake%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n crossguid-%{commit} -N

%patch -P 0 -p0 -b .fix_name
%patch -P 1 -p1 -b .fix_name

%build
%cmake -DCROSSGUID_SOVERSION_STRING:STRING=0 -DCROSSGUID_VERSION_STRING:STRING=0.0 \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/%{name}
%cmake_build

%install
%cmake_install

%check
%__cmake_builddir/%{name}-test

%files
%doc README.md
%license LICENSE
%{_libdir}/libcrossguid2.so.0
%{_libdir}/libcrossguid2.so.0.2.3

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcrossguid2.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
