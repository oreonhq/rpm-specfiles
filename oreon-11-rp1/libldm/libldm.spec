%global source0_hash 61bb2f2367b1df59f818cb96794d1770a0def956bd2c343dccf1425dae3021b5

Name:           libldm
Version:        0.2.5
Release:        3%{?dist}%{?extra_release}
Summary:        A tool to manage Windows dynamic disks

# Automatically converted from old format: LGPLv3+ and GPLv3+ - review is highly recommended.
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
URL:            https://github.com/mdbooth/libldm 
Source0:        https://github.com/mdbooth/libldm/archive/%{name}-%{version}.tar.gz

# All upstream post-0.2.5
Patch:          0001-Add-example-systemd-unit-file.patch
Patch:          0002-ldmtool-fix-NULL-pointer-dereference.patch
Patch:          0003-Add-ability-to-override-device-mapper-UUID.patch
Patch:          0004-src-Fix-declaration-of-ldm_new.patch
Patch:          0005-Update-gtkdocize.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf, automake, libtool
BuildRequires:  glib2-devel >= 2.26.0
BuildRequires:  json-glib-devel >= 0.14.0
BuildRequires:  device-mapper-devel >= 1.0
BuildRequires:  zlib-devel libuuid-devel readline-devel
BuildRequires:  gtk-doc

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

%files
%license COPYING.lgpl COPYING.gpl
%{_libdir}/*.so.*
%{_bindir}/ldmtool
%{_mandir}/man1/ldmtool.1.gz

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/ldm-1.0.pc
%{_datadir}/gtk-doc

%changelog
%autochangelog
