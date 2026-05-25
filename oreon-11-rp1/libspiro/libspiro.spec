Name:           libspiro
Version:        20240903
Release:        4%{?dist}
Summary:        Library to simplify the drawing of beautiful curves

# The files that are used to compile this library are all in GPLv3+
# https://github.com/fontforge/libspiro/issues/8
License:        GPL-3.0-or-later
URL:            https://github.com/fontforge/libspiro/
# Let's use libspiro-dist tarball from upstream as it does not require autoreconf
Source0:        https://github.com/fontforge/libspiro/releases/download/%{version}/libspiro-dist-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: make

%description
This library will take an array of spiro control points and 
convert them into a series of bézier splines which can then 
be used in the myriad of ways the world has come to use béziers. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n libspiro-%{version}

%build
%configure --disable-static
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
make check

%files
%doc README* ChangeLog AUTHORS
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libspiro.pc
%{_mandir}/man3/libspiro.3.gz

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20240903-4
- Import
