%global source0_hash 12b79190593bf480b2d11481b5c2de62bac07f344437a66cd8d887329875c626
Name:           libsidplayfp
Version:        3.1.1
Release:        1%{?dist}
Summary:        SID chip music module playing library
License:        GPL-2.0-or-later AND GPL-2.0-only AND Zlib
URL:            https://github.com/libsidplayfp
Source0:        https://github.com/libsidplayfp/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Provides:       bundled(md5-deutsch-c++)
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libftdi-c++-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This library provides support for playing SID music modules originally
created on Commodore 64 and compatibles. It contains a processing engine
for MOS 6510 machine code and MOS 6581 Sound Interface Device (SID)
chip output. It is used by music player programs like SIDPLAY and
several plug-ins for versatile audio players.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
These are the files needed for compiling programs that use %{name}.

%package devel-doc
Summary:        API documentation for %{name}
BuildArch:      noarch
%description devel-doc
This package contains API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Regenerate autofoo stuff, it is better to always build this from source
rm -r aclocal.m4 build-aux
autoreconf -ivf

%build

%configure --disable-static
make %{_smp_mflags} all doc
%install
%make_install INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libsidplayfp-devel -f %{oreon_filedir}/libsidplayfp-devel.list
%files -n libsidplayfp-devel-doc -f %{oreon_filedir}/libsidplayfp-devel-doc.list

%changelog

%autochangelog
