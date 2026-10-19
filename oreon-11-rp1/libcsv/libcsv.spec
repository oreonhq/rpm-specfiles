%global source0_hash 328ccd918edeeeea52164f7c43500d3ce2f039594c0c81b0aa2e6041bce88ec4
%global commit b1d5212831842ee5869d99bc208a21837e4037d5
%global snapdate 20210820
%bcond autoreconf 1
Name:           libcsv
Version:        3.0.3^%{snapdate}git%{sub %{commit} 1 7}
%global so_version 3
Release:        1%{?dist}
Summary:        Fast and flexible CSV library written in pure ANSI C
License:        LGPL-2.1-or-later
SourceLicense:  %{shrink:
                %{license} AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                GPL-2.0-or-later WITH Libtool-exception AND
                GPL-3.0-or-later WITH Autoconf-exception-generic AND
                LicenseRef-Fedora-UltraPermissive AND
                X11
                }
URL:            https://github.com/rgamble/libcsv
Source0:        https://github.com/rgamble/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
%if %{with autoreconf}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Fast and flexible CSV library written in pure ANSI C that can read and write
CSV data.

%package devel
Summary:        Development files for libcsv
Requires:       libcsv%{?_isa} = %{version}-%{release}
%description devel
The libcsv-devel package contains libraries and header files for
developing applications that use libcsv.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libcsv-%{commit}

%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --disable-static

%build

%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libcsv-devel -f %{oreon_filedir}/libcsv-devel.list

%changelog

%autochangelog
