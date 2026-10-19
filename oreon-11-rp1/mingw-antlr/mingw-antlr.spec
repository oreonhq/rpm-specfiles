%global source0_hash 853aeb021aef7586bda29e74a6b03006bcb565a755c86b66032d8ec31b67dbb9
%{?mingw_package_header}
%global mingw_pkg_name antlr
Summary:        MinGW Windows ANTLR C++ run-time library
Name:			mingw-%{mingw_pkg_name}
Version:		2.7.7
Release:        1%{?dist}
License:		ANTLR-PD
URL:			http://www.antlr.org/
Source0:        http://www.%{mingw_pkg_name}2.org/download/%{mingw_pkg_name}-%{version}.tar.gz
Patch1:			%{mingw_pkg_name}-%{version}-newgcc.patch
Patch2:			mingw-%{mingw_pkg_name}.patch
BuildArch:		noarch
Requires:		pkgconfig
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
ANTLR is a parser generator. This package contains the MinGW Windows
run-time library for ANTLR C++ parsers.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        MinGW Windows ANTLR C++ run-time library
%description -n mingw32-%{mingw_pkg_name}
ANTLR is a parser generator. This package contains the MinGW Windows
run-time library for ANTLR C++ parsers.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:		Static Version of the MinGW Windows ANTLR C++ run-time library
Requires:		mingw32-%{mingw_pkg_name} = %{version}-%{release}
%description -n mingw32-%{mingw_pkg_name}-static
Static version of the MinGW Windows ANTLR run-time library.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        MinGW Windows ANTLR C++ run-time library
%description -n mingw64-%{mingw_pkg_name}
ANTLR is a parser generator. This package contains the MinGW Windows
run-time library for ANTLR C++ parsers.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:		Static Version of the MinGW Windows ANTLR C++ run-time library
Requires:		mingw32-%{mingw_pkg_name} = %{version}-%{release}
%description -n mingw64-%{mingw_pkg_name}-static
Static version of the MinGW Windows ANTLR run-time library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{mingw_pkg_name}-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
%patch -P1
%patch -P2 -p1 -b .mingw
# CRLF->LF
sed -i 's/\r//' LICENSE.txt

%build

%{mingw_configure} --without-examples
pushd lib/cpp
touch NEWS
rm -f {,antlr,src}/Makefile{.in,}
libtoolize -f -c
aclocal -I m4
autoconf
autoheader
automake -a -c
%{mingw_configure} --enable-static
%{mingw_make} %{?_smp_mflags}
popd
%install
pushd lib/cpp
%{mingw_make} install DESTDIR=$RPM_BUILD_ROOT
popd
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libantlr2.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libantlr2.la
mkdir $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 build_win32/scripts/antlr-config $RPM_BUILD_ROOT%{mingw32_bindir}/antlr-config
install -p -m 755 build_win64/scripts/antlr-config $RPM_BUILD_ROOT%{mingw64_bindir}/antlr-config
ln -s %{mingw32_bindir}/antlr-config $RPM_BUILD_ROOT%{_bindir}/%{mingw32_target}-antlr-config
ln -s %{mingw64_bindir}/antlr-config $RPM_BUILD_ROOT%{_bindir}/%{mingw64_target}-antlr-config
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-antlr -f %{oreon_filedir}/mingw32-antlr.list
%files -n mingw32-antlr-static -f %{oreon_filedir}/mingw32-antlr-static.list
%files -n mingw64-antlr -f %{oreon_filedir}/mingw64-antlr.list
%files -n mingw64-antlr-static -f %{oreon_filedir}/mingw64-antlr-static.list

%changelog

%autochangelog
