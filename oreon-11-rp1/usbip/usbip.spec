%global source0_hash 0d3707340b863e1b972c0241334eed076aee37cde8cc0304974f6781f0a67079

%define _legacy_common_support 1

Name:		usbip
License:	GPL-2.0-only
Summary:	USB/IP user-space
Version:	5.7.9
Release:	14%{?dist}
#Source:	https://www.kernel.org/pub/linux/kernel/v5.x/linux-%%{version}.tar.xz
# In the interests of keeping the source rpm from being ridiculously large,
# download the Linux kernel from above and run `extract_usbip.sh <version>`
# in the SOURCE directory.
URL:		https://www.kernel.org
# The kernel modules require working USB and there's no USB for s390x
# See bug #1483403
ExcludeArch:    s390x
Source:		usbip-%{version}.tar.xz
Source1:	usbip-server.service
Source2:	usbip-client.service
Source99:	extract_usbip.sh
Patch0:     usbip-5.5-fix-gcc9.patch
Requires:	kmod(usbip-core.ko)
Requires:	kmod(usbip-host.ko)
Requires:	kmod(vhci-hcd.ko)
Requires:	kernel-modules-extra
Requires:	hwdata
Requires(post):	systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires: make
BuildRequires:	systemd
BuildRequires:	libudev-devel
BuildRequires:	libtool autoconf

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

%description
USB/IP allows you to share USB devices over a network.  With USB/IP, you can
plug a USB device into one computer and use it on a different computer on the
network.

This package contains the user-space tools for USB/IP, both for servers and
clients

%package devel
Summary: USB/IP headers and development libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and static libraries for USB/IP user-space
development

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
%configure --disable-static --with-usbids-dir=%{_datadir}/hwdata
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/libusbip*.la
mkdir -p %{buildroot}%{_unitdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -pm 644 %{SOURCE2} %{buildroot}%{_unitdir}

%post
%systemd_post usbip-client.service usbip-server.service

%preun
%systemd_preun usbip-client.service usbip-server.service

%postun
%systemd_postun_with_restart usbip-client.service usbip-server.service

%files
%license COPYING
%doc README AUTHORS
%{_sbindir}/*
%{_libdir}/*.so.*
%{_mandir}/man8/*
%{_unitdir}/*

%files devel
%license COPYING
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
