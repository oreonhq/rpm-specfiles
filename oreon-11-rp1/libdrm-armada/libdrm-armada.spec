%global source0_hash d14641881fe9fefaf8fa6cf58081d46c86c488b2c33fc9314897568a54ccb69f

%global _configure_disable_silent_rules 1

Name:		libdrm-armada
Version:	2.0.0
Release:	18.20190424git607c697%{?dist}
Summary:	DRM driver for Marvell Armada displays

# Automatically converted from old format: GPLv2 and MIT - review is highly recommended.
License:	GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:		http://git.arm.linux.org.uk/cgit/libdrm-armada.git/
# git clone http://git.arm.linux.org.uk/cgit/libdrm-armada.git/
# cd libdrm-armada
# git reset --hard 607c697
# autoreconf -fi
# ./configure
# make dist
Source0:	libdrm_armada-%{version}.tar.bz2
Patch0:		libdrm-armada-c99.patch

BuildRequires:	pkgconfig(libdrm)
BuildRequires:	gcc
BuildRequires: make

%description
Marvell Armada libdrm buffer object management module.

%package devel
Summary:	Development files for libdrm-armada

%description devel
Development files for libdrm-armada.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libdrm_armada-%{version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%{_libdir}/libdrm_armada.so.0*
%license COPYING

%files devel
%{_includedir}/libdrm
%{_libdir}/libdrm_armada.so
%{_libdir}/pkgconfig/libdrm_armada.pc
%exclude %{_libdir}/libdrm_armada.la

%changelog
%autochangelog
