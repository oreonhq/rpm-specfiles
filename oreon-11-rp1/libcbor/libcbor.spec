Name:		libcbor
Version:	0.13.0
Release:	2%{?dist}
Summary:	A CBOR parsing library

License:	MIT
URL:		http://libcbor.org
Source0:	https://github.com/PJK/%{name}/archive/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	python3-breathe
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	make
BuildRequires:	pkgconfig(cmocka)

%description
libcbor is a C library for parsing and generating CBOR.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{name}-devel contains development libraries and header files for %{name}.

%prep
%autosetup


%build
%cmake -DCMAKE_BUILD_TYPE=Release -DWITH_TESTS=ON
%cmake_build
cd doc
make man


%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man3
cp doc/build/man/libcbor.3 %{buildroot}%{_mandir}/man3/


%check
%ctest


%files
%license LICENSE.md
%doc README.md
%{_libdir}/libcbor.so.0.13{,.*}

%files devel
%{_includedir}/cbor.h
%{_includedir}/cbor
%{_libdir}/libcbor.so
%{_libdir}/pkgconfig/libcbor.pc
%{_libdir}/cmake/libcbor
%{_mandir}/man3/libcbor.3{,.*}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13.0-2
- Prepare for Oreon 11 (RP1)
