%global source0_hash 4215e7876e786dcdbf5ae14a7c0b9549b7817cdf6f5ce0debe1d1674e0d1c900
%global rescan_script rescan-scsi-bus.sh
%global _udevlibdir %{_prefix}/lib/udev
Summary:        Utilities for devices that use SCSI command sets
Name:    sg3_utils
Version: 1.49
Release:        1%{?dist}
License: GPL-2.0-or-later AND BSD-2-Clause
URL:     https://sg.danny.cz/sg/sg3_utils.html
Source0:        https://src.fedoraproject.org/repo/pkgs/sg3_utils/sg3_utils-1.49.tar.xz/sha512/00c76d367e076feff460b619d05a043ab6404642043c000f7a5f93ba503e0bbcc53ebe408d405d252b155197bf456fcc3a8eb8519153825a9c616b2ed8ba9b10/sg3_utils-1.49.tar.xz
Source1: scsi-rescan.8
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
Collection of Linux utilities for devices that use the SCSI command set.
Includes utilities to copy data based on "dd" syntax and semantics (called
sg_dd, sgp_dd and sgm_dd); check INQUIRY data and VPD pages (sg_inq); check
mode and log pages (sginfo, sg_modes and sg_logs); spin up and down
disks (sg_start); do self tests (sg_senddiag); and various other functions.
See the README, CHANGELOG and COVERAGE files. Requires the linux kernel 2.4
series or later. In the 2.4 series SCSI generic device names (e.g. /dev/sg0)
must be used. In the 2.6 series other device names may be used as
well (e.g. /dev/sda).

Warning: Some of these tools access the internals of your system
and the incorrect usage of them may render your system inoperable.

%package libs
Summary: Shared library for %{name}
%description libs
This package contains the shared library for %{name}.

%package devel
Summary: Development library and header files for the sg3_utils library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the %{name} library and its header files for
developing applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i 's|55-scsi-sg3_id.rules|61-scsi-sg3_id.rules|' scripts/*.rules
sed -i 's|58-scsi-sg3_symlink.rules|63-scsi-sg3_symlink.rules|' scripts/*.rules
sed -i 's|59-scsi-cciss_id.rules|65-scsi-cciss_id.rules|' scripts/*.rules
sed -i 's|59-fc-wwpn-id.rules|63-fc-wwpn-id.rules|' scripts/*.rules
%make_build
%install
%make_install
rm -rf %{buildroot}%{_libdir}/*.la
install -p -m 755 scripts/%{rescan_script} %{buildroot}%{_bindir}
( cd %{buildroot}%{_bindir}; ln -sf %{rescan_script} scsi-rescan )
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_udevlibdir}
install -p -m 644 scripts/00-scsi-sg3_config.rules %{buildroot}%{_udevrulesdir}
install -p -m 644 scripts/40-usb-blacklist.rules %{buildroot}%{_udevrulesdir}
install -p -m 644 scripts/55-scsi-sg3_id.rules %{buildroot}%{_udevrulesdir}/61-scsi-sg3_id.rules
install -p -m 644 scripts/58-scsi-sg3_symlink.rules %{buildroot}%{_udevrulesdir}/63-scsi-sg3_symlink.rules
install -p -m 644 scripts/59-scsi-cciss_id.rules %{buildroot}%{_udevrulesdir}/65-scsi-cciss_id.rules
install -p -m 644 scripts/59-fc-wwpn-id.rules %{buildroot}%{_udevrulesdir}/63-fc-wwpn-id.rules
install -p -m 755 scripts/fc_wwpn_id %{buildroot}%{_udevlibdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sg3_utils-libs -f %{oreon_filedir}/sg3_utils-libs.list
%files -n sg3_utils-devel -f %{oreon_filedir}/sg3_utils-devel.list

%changelog

%autochangelog
