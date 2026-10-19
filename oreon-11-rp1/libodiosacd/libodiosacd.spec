%global source0_hash 90d9970505c6b730222910a83d61b0a66f83f94e4e7d7ad5e2fc238705dd6e20
%global forgeurl https://github.com/tari01/libodiosacd
Name:           libodiosacd
Version:        25.4.1
Release:        1%{?dist}
Summary:        SACD decoder shared library
License:        GPL-3.0-or-later
URL:            https://tari.in/www/software/libodiosacd/
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-fedora.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
The Odio SACD shared library is a decoding engine which takes a Super Audio CD
source and extracts a 24-bit high resolution wave file. It handles both DST and
DSD streams.

The library reads the following input:
- SACD image files (*.iso)
- Sony DSF files (*.dsf)
- Philips DSDIFF files (*.dff)

Supported output sample rates:
- 88.2kHz
- 176.4kHz

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod -x COPYING Makefile src/*.{c,h} src/*/*.{c,h}

%build

%set_build_flags
%make_build O=2
%install
install -dm755 %{buildroot}%{_libdir}
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libodiosacd-devel -f %{oreon_filedir}/libodiosacd-devel.list

%changelog

%autochangelog
