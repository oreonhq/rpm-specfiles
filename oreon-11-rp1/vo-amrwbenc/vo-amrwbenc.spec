%global source0_hash 5652b391e0f0e296417b841b02987d3fd33e6c0af342c69542cbb016a71d9d4e
%global sovermajor 0
Name:           vo-amrwbenc
Version:        0.1.3
Release:        1%{?dist}
Summary:        VisualOn AMR-WB encoder library
License:        Apache-2.0
URL:            http://opencore-amr.sourceforge.net/
Source0:        http://downloads.sourceforge.net/opencore-amr/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This library contains an encoder implementation of the Adaptive
Multi Rate Wideband (AMR-WB) audio codec. The library is based
on a codec implementation by VisualOn as part of the Stagefright
framework from the Google Android project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/libvo-amrwbenc.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n vo-amrwbenc-devel -f %{oreon_filedir}/vo-amrwbenc-devel.list

%changelog

%autochangelog
