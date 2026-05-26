# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 d6b9a41690d540e58d1e99c26ac8db37336c849ef6a03f96ea48ca2fe334dbfa
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global rescan_script rescan-scsi-bus.sh
%global _udevlibdir %{_prefix}/lib/udev

Summary: Utilities for devices that use SCSI command sets
Name:    sg3_utils
Version: 1.48
Release: 8%{?dist}
License: GPL-2.0-or-later AND BSD-2-Clause
URL:     https://sg.danny.cz/sg/sg3_utils.html
Source0: https://sg.danny.cz/sg/p/sg3_utils-%{version}.tar.xz
Source1: scsi-rescan.8
# https://github.com/doug-gilbert/sg3_utils/pull/43
# scripts/rescan-scsi-bus.sh: fix multipath resize without update
Patch0: 0001-rescan-scsi-bus.sh-fix-multipath-resize-without-upda.patch
# https://github.com/doug-gilbert/sg3_utils/pull/44
# scripts/rescan-scsi-bus.sh: remove /tmp/rescan-scsi-mpath-info.txt
Patch1: 0002-rescan-scsi-bus.sh-remove-tmp-rescan-scsi-mpath-info.patch
# https://github.com/doug-gilbert/sg3_utils/issues/46
# scripts/rescan-scsi-bus.sh: -r flag unmounts active root disk
Patch2: 0003-rescan-scsi-bus.sh-fix-for-github.com-doug-gilbert-s.patch
# https://github.com/doug-gilbert/sg3_utils/pull/47
Patch3: udev_rules-avoid_spurious_warning_for_non-SCSI_devices.patch
# https://github.com/doug-gilbert/sg3_utils/pull/68
# rescan-scsi-bus.sh Correctly read RMB bit on enquiry
Patch4: 0004-rescan-scsi-bus.sh-Correctly-read-RMB-bit-on-enquiry.patch
# https://github.com/doug-gilbert/sg3_utils/pull/68
# rescan-scsi-bus.sh Replace 'which' with build in 'command -v'
Patch5: 0005-rescan-scsi-bus.sh-Replace-which-with-build-in-comma.patch
# https://github.com/doug-gilbert/sg3_utils/pull/69
# Update sg_safte.c to update short option of version
Patch6: 0006-Update-sg_safte.c-to-update-short-option-of-version.patch
# https://github.com/doug-gilbert/sg3_utils/pull/56
# Update sg_rdac.c to accept --help or -h without error
Patch7: 0007-Update-sg_rdac.c-to-accept--help-or--h-without-erro.patch
# https://github.com/doug-gilbert/sg3_utils/pull/49
# sg_inq: fix missing output fields in --export format
Patch8: 0008-sg_inq-fix-missing-output-fields-in--export-format.patch
# https://github.com/doug-gilbert/sg3_utils/pull/49
# sg_inq: re-add Unit serial number field
#Patch9: 0009-sg_inq-re-add-Unit-serial-number-field.patch

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: make
BuildRequires: gcc
BuildRequires: systemd


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
%oreon_verify_sources
%autosetup -p 1


%build
%configure --disable-static

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# Fix filename references to other udev rules
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

# install all extra udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_udevlibdir}
install -p -m 644 scripts/00-scsi-sg3_config.rules %{buildroot}%{_udevrulesdir}
install -p -m 644 scripts/40-usb-blacklist.rules %{buildroot}%{_udevrulesdir}
# need to run after 60-persistent-storage.rules
install -p -m 644 scripts/55-scsi-sg3_id.rules %{buildroot}%{_udevrulesdir}/61-scsi-sg3_id.rules
# need to run after 62-multipath.rules
install -p -m 644 scripts/58-scsi-sg3_symlink.rules %{buildroot}%{_udevrulesdir}/63-scsi-sg3_symlink.rules
install -p -m 644 scripts/59-scsi-cciss_id.rules %{buildroot}%{_udevrulesdir}/65-scsi-cciss_id.rules
install -p -m 644 scripts/59-fc-wwpn-id.rules %{buildroot}%{_udevrulesdir}/63-fc-wwpn-id.rules
install -p -m 755 scripts/fc_wwpn_id %{buildroot}%{_udevlibdir}


%files
%license BSD_LICENSE COPYING
%doc AUTHORS COVERAGE CREDITS ChangeLog README README.sg_start
%{_bindir}/scsi_*
%{_bindir}/sg_*
%{_bindir}/rescan-scsi-bus.sh
%{_bindir}/scsi-rescan
%{_bindir}/sginfo
%{_bindir}/sgm_dd
%{_bindir}/sgp_dd
%{_mandir}/man8/scsi_*.8*
%{_mandir}/man8/sg_*.8*
%{_mandir}/man8/rescan-scsi-bus.sh.8*
%{_mandir}/man8/scsi-rescan.8*
%{_mandir}/man8/sginfo.8*
%{_mandir}/man8/sgm_dd.8*
%{_mandir}/man8/sgp_dd.8*
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}_json.8*
%{_udevrulesdir}/00-scsi-sg3_config.rules
%{_udevrulesdir}/61-scsi-sg3_id.rules
%{_udevrulesdir}/63-scsi-sg3_symlink.rules
%{_udevrulesdir}/63-fc-wwpn-id.rules
%{_udevrulesdir}/65-scsi-cciss_id.rules
%{_udevrulesdir}/40-usb-blacklist.rules
%{_udevlibdir}/fc_wwpn_id

%files libs
%doc BSD_LICENSE COPYING
%{_libdir}/libsgutils2-%{version}.so.*

%files devel
%{_includedir}/scsi/*.h
%{_libdir}/libsgutils2.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.48-8
- Prepare for Oreon 11 (RP1)
