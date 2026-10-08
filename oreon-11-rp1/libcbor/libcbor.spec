%global source0_hash a8c1516e741562cf95aa4479c64916c3d4d2623e24fdc35e414e2320e7300aae

Name:		libcbor
Version:	0.14.0
Release:	1%{?dist}
Summary:	A CBOR parsing library

License:	MIT
URL:		http://libcbor.org
Source0:        https://github.com/PJK/%{name}/archive/v%{version}.tar.gz#/libcbor-%{version}.tar.gz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
sed -i -e 's|^LAYOUT_FILE *=.*|LAYOUT_FILE =|' -e 's|^HTML_EXTRA_STYLESHEET *=.*|HTML_EXTRA_STYLESHEET =|' Doxyfile


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
%autochangelog
