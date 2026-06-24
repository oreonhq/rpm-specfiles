%global source0_hash none

Name:           cln
Version:        1.3.6
Release:        10%{?dist}
Summary:        Class Library for Numbers

License:        GPL-2.0-or-later
URL:            http://www.ginac.de/CLN/
Source0:        http://www.ginac.de/CLN/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  texi2html
%if 0%{?fedora} && 0%{?fedora} > 20
BuildRequires:  perl(Unicode::EastAsianWidth)
%endif
BuildRequires:  texinfo-tex
BuildRequires: make

%description
A collection of C++ math classes and functions, which are designed for
memory and speed efficiency, and enable type safety and algebraic
syntax.

%package        devel
Summary:        Development files for programs using the CLN library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    devel
A collection of C++ math classes and functions, which are designed for
memory and speed efficiency, and enable type safety and algebraic
syntax.

This package is necessary if you wish to develop software based on
the CLN library.

%ifarch %{arm}
%global XFLAGS %{optflags} -DNO_ASM
%else
%global XFLAGS %{optflags}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static CXXFLAGS="%{XFLAGS}" CFLAGS="%{XFLAGS}"
make %{?_smp_mflags}
make pdf
make html

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/pi.*

%check
make %{_smp_mflags} check

%ldconfig_scriptlets

%files
%doc COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/cln.pc
%{_includedir}/cln/
%{_infodir}/*.info*
%doc doc/cln.pdf doc/cln.html

%changelog
%autochangelog

