%global source0_hash c81c81bba8a7644c84932225f018b5088743a22999c6d82a2b5f5cd1e6942b74

# Header-only library.
%global debug_package %{nil}

Name:           cppzmq
Version:        4.10.0
Release:        %autorelease
Summary:        Header-only C++ binding for libzmq

License:        MIT
URL:            https://zeromq.org
Source0:        https://github.com/zeromq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  (cmake(Catch2) >= 2.13.9 with cmake(Catch2) < 3)

%global _description \
cppzmq is a C++ binding for libzmq. \
\
cppzmq maps the libzmq C API to C++ concepts. In particular, it is type-safe, \
provides exception-based error handling, and provides RAII-style classes that \
automate resource management. cppzmq is a light-weight, header-only binding.

%description %{_description}

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

Requires:       pkgconfig(libzmq)

%description devel %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/zmq*.hpp
%{_datadir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
