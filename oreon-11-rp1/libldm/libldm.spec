%global source0_hash 61bb2f2367b1df59f818cb96794d1770a0def956bd2c343dccf1425dae3021b5
Name:           libldm
Version:        0.2.5
Release:        1%{?dist}
Summary:        A tool to manage Windows dynamic disks
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
URL:            https://github.com/mdbooth/libldm 
Source0:        https://github.com/mdbooth/libldm/archive/%{name}-%{version}.tar.gz
Patch:          0001-Add-example-systemd-unit-file.patch
Patch:          0002-ldmtool-fix-NULL-pointer-dereference.patch
Patch:          0003-Add-ability-to-override-device-mapper-UUID.patch
Patch:          0004-src-Fix-declaration-of-ldm_new.patch
Patch:          0005-Update-gtkdocize.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  device-mapper-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  json-glib-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
libldm is a library for managing Microsoft Windows dynamic disks, which use
Microsoft's LDM metadata. It can inspect them, and also create and remove
device-mapper block devices which can be mounted. It includes ldmtool, which
exposes this functionality as a command-line tool.

libldm is released under LGPLv3+. ldmtool is released under GPLv3+.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{name}-%{version}
sed -i -e 's/-Werror //' src/Makefile.*
gtkdocize
autoreconf -i

%build

%configure --disable-static --enable-gtk-doc
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libldm-devel -f %{oreon_filedir}/libldm-devel.list

%changelog

%autochangelog
