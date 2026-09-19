%global source0_hash c045c7a33a00affbfeb11066fa502c03992e474a62ba95977aad06dbc14c6829

Name:           lightning
Version:        2.2.3
Release:        6%{?dist}
Summary:        Library for generating assembly code on run time
License:        LGPL-3.0-or-later
URL:            http://www.gnu.org/software/lightning/lightning.html
Source0:        ftp://ftp.gnu.org/gnu/lightning/lightning-%{version}.tar.gz

BuildRequires:  texinfo, gcc
BuildRequires:  binutils-devel
BuildRequires:  make

%description
GNU lightning is a library to aid in making portable programs
that compiles assembly code at run time.

%package devel
Summary:        Header for the lightning package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains development header and libraries of the
ligthing package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --enable-static=no --enable-shared=yes --with-gnu-ld --with-pic
%make_build V=1 CFLAGS="%{optflags} -fno-strict-aliasing"

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
mv $RPM_BUILD_ROOT%{_includedir}/lightning.h $RPM_BUILD_ROOT%{_includedir}/lightning

%check
make check V=1 CFLAGS="-g -fno-strict-aliasing -fPIC"

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS README THANKS
%license COPYING COPYING.DOC COPYING.LESSER
%{_libdir}/liblightning.so.2.0.2
%{_libdir}/liblightning.so.2

%files devel
%{_libdir}/liblightning.so
%{_includedir}/lightning/
%{_infodir}/lightning.info.*
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
