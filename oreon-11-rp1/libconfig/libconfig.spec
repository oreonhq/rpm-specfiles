%global source0_hash none

%bcond_without check

Name:                   libconfig
Summary:                C/C++ configuration file library
Version:                1.8.2
Release:                2%{?dist}
# lib/grammar.* are GPL-3.0-or-later WITH Bison-exception-2.2
License:                LGPL-2.1-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
URL:                    http://www.hyperrealm.com/libconfig/
Source0:                https://hyperrealm.github.io/%name/dist/%name-%version.tar.gz
# Generated from libconfig 1.8.2 on Fedora 44 x86_64 (2025-12-17)
Source1:                libconfig-%version.pdf
# Helper script to generate Source1 (locally)
Source2:                generate-pdf.sh

BuildRequires:          gcc, gcc-c++
BuildRequires:          texinfo
BuildRequires:          bison, flex
BuildRequires: make

%description
Libconfig is a simple library for manipulating structured configuration
files. This file format is more compact and more readable than XML. And
unlike XML, it is type-aware, so it is not necessary to do string parsing
in application code.


%package devel
Summary:                Development files for libconfig
Requires:               %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for developing software against
libconfig.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
iconv -f iso-8859-1 -t utf-8 -o AUTHORS{.utf8,}
mv AUTHORS{.utf8,}


%build
%configure \
  --disable-silent-rules \
  --disable-static

make %{?_smp_mflags}


%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
install -p %{SOURCE1} doc/


%if %{with check}
%check
make check
%endif


%ldconfig_scriptlets

%files
%license COPYING.LIB
%doc AUTHORS ChangeLog README
%{_libdir}/libconfig*.so.15*


%files devel
%doc doc/libconfig-%version.pdf
%{_includedir}/libconfig*
%{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}++
%{_libdir}/libconfig*.so
%{_libdir}/pkgconfig/libconfig*.pc
%{_infodir}/libconfig.info*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.2-2
- Import
