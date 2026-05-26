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
# oreon url source checksums begin
%global source0_sha256 098f824a495a1a837d56ae17e07b3f721ac86f8dbaf58896a389923458522108
%global source0_file capnproto-c++-1.3.0.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/capnproto-c++-1.3.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "098f824a495a1a837d56ae17e07b3f721ac86f8dbaf58896a389923458522108" || { echo "oreon: Source0 SHA256 mismatch for capnproto-c++-1.3.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
