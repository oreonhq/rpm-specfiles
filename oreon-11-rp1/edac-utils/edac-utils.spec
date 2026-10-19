%global source0_hash 2a027dbde6c3095807c9fbfa0025bedad38fc839e9967707c1986089ff4c8750
Name:           edac-utils
Version:        0.18
%global so_version 1
Release:        1%{?dist}
Summary:        Userspace helper for kernel EDAC drivers
License:        GPL-2.0-or-later
SourceLicense:  %{shrink:
                %{license} AND
                FSFUL AND
                GPL-2.0-or-later WITH Autoconf-exception-macro AND
                X11}
URL:            https://github.com/grondo/edac-utils
Source0:        https://github.com/grondo/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        edac.service
ExcludeArch:    %{ix86}
Patch:          %{url}/pull/13.patch
Requires:       libedac = %{version}-%{release}
Requires:       edac-util = %{version}-%{release}
Requires:       edac-ctl = %{version}-%{release}
%global common_description %{expand:
EDAC (Error Detection and Correction) is a set of Linux kernel modules that
handle reporting of hardware-related errors. Currently these modules mainly
handle detection of ECC memory errors for many x86 and x86-64 chipsets and PCI
bus parity errors.
The edac-utils project currently has three components: libedac, edac-util, and
edac-ctl. The libedac library presents a standard API for reading EDAC error
counts and other information from sysfs, and edac-util uses this API to
generate standard reports from the commandline. The edac-ctl utility is a perl
script which uses config files to load the appropriate EDAC driver for a given
chipset and register motherboard DIMM labels if they are configured. An init
script is also provided which uses edac-ctl to initialize EDAC at system
startup.}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libsysfs-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description %{common_description}

This is a metapackage that installs all three components.

%package -n libedac
Summary:        Standard API for reading EDAC error counts from sysfs
%description -n libedac %{common_description}

This package provides the libedac library.

%package -n libedac-devel
Summary:        Development files for libedac
Requires:       libedac%{?_isa} = %{version}-%{release}
Provides:       edac-utils-devel%{?_isa} = %{version}-%{release}
Provides:       edac-utils-devel = %{version}-%{release}
Obsoletes:      edac-utils-devel < 0.18-18
%description -n libedac-devel %{common_description}

This package contains the development headers and libraries and the man page
for libedac.

%package -n edac-util
Summary:        Command-line tool to generate standard EDAC reports
Requires:       libedac%{?_isa} = %{version}-%{release}
%description -n edac-util %{common_description}

This package provides the edac-util command-line tool.

%package -n edac-ctl
Summary:        Script to load EDAC driver and register DIMM labels
%ifarch %{ix86} x86_64 ia64 aarch64 riscv64
Requires:       dmidecode
%endif
Requires:       hwdata
Requires:       kmod
%description -n edac-ctl %{common_description}

This package provides the edac-ctl script and the edac service.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
autoreconf --force --install --verbose
%configure --disable-static

%build

%make_build
%install
%make_install
install -D -p -m 0644 '%{SOURCE1}' '%{buildroot}%{_unitdir}/edac.service'
rm -f '%{buildroot}%{_sysconfdir}/init.d/edac'
install -d -m 0755 '%{buildroot}%{_sysconfdir}/edac/labels.d' \
    '%{buildroot}%{_sysconfdir}/edac/mainboard'
%oreon_autofiles libedac usr/*/lib*.so.*
%oreon_autofiles libedac-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles edac-util usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles edac-ctl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post -n edac-ctl

%systemd_post edac.service
%preun -n edac-ctl

%systemd_preun edac.service
%postun -n edac-ctl

%systemd_postun_with_restart edac.service
%files -f %{oreon_filedir}/main.list
%files -n libedac -f %{oreon_filedir}/libedac.list
%files -n libedac-devel -f %{oreon_filedir}/libedac-devel.list
%files -n edac-util -f %{oreon_filedir}/edac-util.list
%files -n edac-ctl -f %{oreon_filedir}/edac-ctl.list

%changelog

%autochangelog
