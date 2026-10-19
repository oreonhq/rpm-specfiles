%global source0_hash d14641881fe9fefaf8fa6cf58081d46c86c488b2c33fc9314897568a54ccb69f
%global _configure_disable_silent_rules 1
Name:		libdrm-armada
Version:	2.0.0
Release:        1%{?dist}
Summary:        DRM driver for Marvell Armada displays
License:	GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:		http://git.arm.linux.org.uk/cgit/libdrm-armada.git/
Source0:        libdrm_armada-%{version}.tar.bz2
Patch0:		libdrm-armada-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libdrm)
# /oreon:deps
%description
Marvell Armada libdrm buffer object management module.

%package devel
Summary:	Development files for libdrm-armada
%description devel
Development files for libdrm-armada.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libdrm_armada-%{version}
%oreon_prep
%build

%configure
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdrm-armada-devel -f %{oreon_filedir}/libdrm-armada-devel.list

%changelog

%autochangelog
