%global source0_hash 34997b3f47d6683ac31d64cfc7ac7df4ff0b8d62982ba3c5d9584f0e48f40ad3
Name:		libzbd
Version:	2.0.4
Release:        9%{?dist}
Summary:        A library to control zoned block devices
License:	LGPL-3.0-or-later AND GPL-3.0-or-later
URL:		https://github.com/westerndigitalcorporation/%{name}
Source0:        https://github.com/westerndigitalcorporation/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
libzbd is a library providing functions simplifying the management and
use of zoned block devices using the kernel ioctl interface.

# Development headers package
%package devel
Summary: Development header files for libzbd
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides development header files for libzbd.

# Command line tools package
%package cli-tools
Summary: Command line tools using libzbd
Requires: %{name}%{?_isa} = %{version}-%{release}
%description cli-tools
This package provides command line tools using libzbd.

# Graphic tools package
%package gtk-tools
Summary: GTK tools using libzbd
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gtk-tools
This package provides GTK-based graphical tools using libzbd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

sh autogen.sh
%configure --libdir="%{_libdir}" --includedir="%{_includedir}"
%make_build
%install
%make_install PREFIX=%{_prefix}
chmod -x ${RPM_BUILD_ROOT}%{_mandir}/man8/*.8*
find ${RPM_BUILD_ROOT} -name '*.la' -delete
desktop-file-validate %{buildroot}/%{_datadir}/applications/gzbd.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/gzbd-viewer.desktop
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libzbd-devel -f %{oreon_filedir}/libzbd-devel.list
%files -n libzbd-cli-tools -f %{oreon_filedir}/libzbd-cli-tools.list
%files -n libzbd-gtk-tools -f %{oreon_filedir}/libzbd-gtk-tools.list

%changelog

%autochangelog
