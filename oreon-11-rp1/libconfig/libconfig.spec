%global source0_hash e59ffb902dd5731d5d4e4fb81d3b989697615feab72dfd7c30618167b91a42ee
%bcond_without check
Name:                   libconfig
Summary:        C/C++ configuration file library
Version:                1.8.2
Release:        1%{?dist}
License:                LGPL-2.1-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
URL:                    http://www.hyperrealm.com/libconfig/
Source0:        https://hyperrealm.github.io/%{name}/dist/%{name}-%{version}.tar.gz
Source1:                libconfig-%version.pdf
Source2:                generate-pdf.sh
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

make check
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libconfig-devel -f %{oreon_filedir}/libconfig-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.2-2
- Import
