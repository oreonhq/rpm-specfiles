Name:		libzpc
Version:	1.4.1
Release:	%autorelease
Summary:	Open Source library for the IBM Z Protected-key crypto feature

License:	MIT
Url:		https://github.com/opencryptoki/libzpc
Source0:        https://github.com/opencryptoki/libzpc/archive/v1.4.1/libzpc-1.4.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 2a361a3a239afc3f40e6dbac28da4503f5103338d7b17de41ac2c2979d862d1d
%global source0_file libzpc-1.4.1.tar.gz
# oreon url source checksums end

ExclusiveArch:	s390x
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	g++
BuildRequires:	make
BuildRequires:	json-c-devel

#Additional prerequisites for building the test program: libjson-c devel 
#Additional prereqs for building the html and latex doc: doxygen >= 1.8.17, latex, bibtex

# Be explicit about the soversion in order to avoid unintentional changes.
%global soversion 1

%description
The IBM Z Protected-key Crypto library libzpc is an open-source library
targeting the 64-bit Linux on IBM Z (s390x) platform. It provides interfaces
for cryptographic primitives. The underlying implementations make use of
z/Architecture's extensive performance-boosting hardware support and its
protected-key feature which ensures that key material is never present in
main memory at any time.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libzpc-1.4.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2a361a3a239afc3f40e6dbac28da4503f5103338d7b17de41ac2c2979d862d1d" || { echo "oreon: Source0 SHA256 mismatch for libzpc-1.4.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup %{name}-%{version}

# The following options can be passed to cmake:
#   -DCMAKE_INSTALL_PREFIX=<path> : 
#        Change the install prefix from `/usr/local/` to `<path>`.
#   -DCMAKE_BUILD_TYPE=<type> : Choose predefined build options. 
#        The choices for `<type>` are `Debug`, `Release`, `RelWithDebInfo`, 
#        and `MinSizeRel`.
#   -DBUILD_SHARED_LIBS=ON : Build a shared object (instead of an archive).
#   -DBUILD_TEST=ON : Build the test program.
#   -DBUILD_DOC=ON : Build the html and latex doc.
%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%doc README.md CHANGES.md
%license LICENSE
%{_libdir}/%{name}.so.%{soversion}*


%files devel
%{_includedir}/zpc/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.1-1
- Import
