%global source0_hash 651e88af3c8189d4faed538bee3affde360eb4698a70505765fc7e5653f5eb23
%global commit0 5e9be272f96e00f15a2f3c5f8ba7e124862aec38
Name:           aribb24
Version:        1.0.3
Release:        1%{?dist}
Summary:        A library for ARIB STD-B24
License:        LGPL-3.0-only
URL:            https://github.com/nkoriyama/aribb24
Source0:        https://github.com/nkoriyama/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
A library for ARIB STD-B24, decoding JIS 8 bit characters and parsing MPEG-TS
stream.

%package devel
Summary:        Development files for the ARIB STD-B24 library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files and headers for the ARIB STD-B24 library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n aribb24-%{commit0}

%build

autoreconf -vif
%configure --disable-static
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{name}.la
rm -fr %{buildroot}%{_docdir}/%{name}
%oreon_autofiles aribb24-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n aribb24-devel -f %{oreon_filedir}/aribb24-devel.list

%changelog

%autochangelog
