# Force out of source build
%undefine __cmake_in_source_build

%global modulename %{name}-c++

Name:           capnproto
Version:        1.3.0
Release:        4%{?dist}
Summary:        A data interchange format and capability-based RPC system

License:        MIT
URL:            https://capnproto.org
Source0:        https://capnproto.org/%{modulename}-%{version}.tar.gz

# We need C++
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.10

# Ensure that we use matching version of libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Cap’n Proto is an insanely fast data interchange format
and capability-based RPC system. Think JSON, except binary.
Or think Protocol Buffers, except faster. In fact, in benchmarks,
Cap’n Proto is INFINITY TIMES faster than Protocol Buffers.

This package contains the schema compiler and command-line
encoder/decoder tools.

%package        libs
Summary:        Libraries for %{name}

%description    libs
The %{name}-libs package contains the libraries for using %{name}
in applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{modulename}-%{version} -p2


%conf
# The tests are randomly failing due to poor sparsing support in the build system
export CFLAGS="%{build_cflags} -DHOLES_NOT_SUPPORTED=1"
export CXXFLAGS="%{build_cxxflags} -DHOLES_NOT_SUPPORTED=1"

%cmake -DBUILD_TESTING=ON


%build
%cmake_build


%check
%ctest


%install
%cmake_install
find %{buildroot} -name '*.la' -delete


%files
%{_bindir}/capnp
%{_bindir}/capnpc
%{_bindir}/capnpc-c++
%{_bindir}/capnpc-capnp

%files libs
%license LICENSE.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/CapnProto/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-4
- Prepare for Oreon 11 (RP1)
