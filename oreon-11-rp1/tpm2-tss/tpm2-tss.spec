# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 37f1580200ab78305d1fc872d89241aaee0c93cbe85bc559bf332737a60d3be8
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond_with rc
%if %{with rc}
%global candidate rc2
%endif

Name:          tpm2-tss
Version:       4.1.3
Release:       9%{?candidate:.%{candidate}}%{?dist}
Summary:       TPM2.0 Software Stack

License:       BSD-2-Clause
URL:           https://github.com/tpm2-software/tpm2-tss
Source0:        https://github.com/tpm2-software/tpm2-tss/releases/download/4.1.3/tpm2-tss-4.1.3.tar.gz
Source1:       tpm2-tss-systemd-sysusers.conf
# doxygen crash
Patch0:        tpm2-tss-3.0.0-doxygen.patch
# Do not use <openssl/engine.h> (fixed upstream for 4.2)
Patch1:        tpm2-tss-4.1.3-openssl-no-engine.patch

%global udevrules_prefix 60-

%if %{with rc}
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
%endif
BuildRequires: make
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: json-c-devel
BuildRequires: libcurl-devel
BuildRequires: libgcrypt-devel
BuildRequires: libusb1-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: libuuid-devel

%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

%package fapi
Summary:       High-level TPM2.0 Software Stack
Requires:      %{name}%{_isa} = %{version}-%{release}

%description fapi
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

This package provides the high-level "Feature API" library.

%prep
%oreon_verify_sources
%autosetup -n %{name}-%{version}%{?candidate:-%{candidate}} -p1

%build
# Use built-in tpm-udev.rules, with specified installation path and prefix.
%configure --disable-static --disable-silent-rules \
           --with-udevrulesdir=%{_udevrulesdir} --with-udevrulesprefix=%{udevrules_prefix} \
           --with-runstatedir=%{_rundir} --with-tmpfilesdir=%{_tmpfilesdir} --with-sysusersdir=%{_sysusersdir}

# This is to fix Rpath errors. Taken from https://fedoraproject.org/wiki/Packaging:Guidelines#Removing_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name \*.la -delete
rm %{buildroot}%{_sysusersdir}/tpm2-tss.conf
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/tpm2-tss.conf


%ldconfig_scriptlets

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_sysconfdir}/tpm2-tss/
%{_libdir}/libtss2-mu.so.0*
%{_libdir}/libtss2-sys.so.1*
%{_libdir}/libtss2-esys.so.0*
%{_libdir}/libtss2-policy.so.0*
%{_libdir}/libtss2-rc.so.0*
%{_libdir}/libtss2-tctildr.so.0*
%{_libdir}/libtss2-tcti-cmd.so.0*
%{_libdir}/libtss2-tcti-device.so.0*
%{_libdir}/libtss2-tcti-mssim.so.0*
%{_libdir}/libtss2-tcti-pcap.so.0*
%{_libdir}/libtss2-tcti-i2c-helper.so.0*
%{_libdir}/libtss2-tcti-spidev.so.0*
%{_libdir}/libtss2-tcti-spi-helper.so.0*
%{_libdir}/libtss2-tcti-spi-ltt2go.so.0*
%{_libdir}/libtss2-tcti-swtpm.so.0*
%{_sysusersdir}/tpm2-tss.conf
%{_udevrulesdir}/%{udevrules_prefix}tpm-udev.rules

%files fapi
%{_libdir}/libtss2-fapi.so.1*
%{_tmpfilesdir}/tpm2-tss-fapi.conf

%package        devel
Summary:        Headers and libraries for building apps that use tpm2-tss 
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       %{name}-fapi%{_isa} = %{version}-%{release}

%description    devel
This package contains headers and libraries required to build applications that
use tpm2-tss.

%files devel
%{_includedir}/tss2/
%{_libdir}/libtss2-mu.so
%{_libdir}/libtss2-sys.so
%{_libdir}/libtss2-esys.so
%{_libdir}/libtss2-fapi.so
%{_libdir}/libtss2-policy.so
%{_libdir}/libtss2-rc.so
%{_libdir}/libtss2-tctildr.so
%{_libdir}/libtss2-tcti-cmd.so
%{_libdir}/libtss2-tcti-device.so
%{_libdir}/libtss2-tcti-mssim.so
%{_libdir}/libtss2-tcti-pcap.so
%{_libdir}/libtss2-tcti-i2c-helper.so
%{_libdir}/libtss2-tcti-spidev.so
%{_libdir}/libtss2-tcti-spi-helper.so
%{_libdir}/libtss2-tcti-spi-ltt2go.so
%{_libdir}/libtss2-tcti-swtpm.so
%{_libdir}/pkgconfig/tss2-mu.pc
%{_libdir}/pkgconfig/tss2-sys.pc
%{_libdir}/pkgconfig/tss2-esys.pc
%{_libdir}/pkgconfig/tss2-fapi.pc
%{_libdir}/pkgconfig/tss2-policy.pc
%{_libdir}/pkgconfig/tss2-rc.pc
%{_libdir}/pkgconfig/tss2-tctildr.pc
%{_libdir}/pkgconfig/tss2-tcti-cmd.pc
%{_libdir}/pkgconfig/tss2-tcti-device.pc
%{_libdir}/pkgconfig/tss2-tcti-mssim.pc
%{_libdir}/pkgconfig/tss2-tcti-pcap.pc
%{_libdir}/pkgconfig/tss2-tcti-i2c-helper.pc
%{_libdir}/pkgconfig/tss2-tcti-spidev.pc
%{_libdir}/pkgconfig/tss2-tcti-spi-helper.pc
%{_libdir}/pkgconfig/tss2-tcti-spi-ltt2go.pc
%{_libdir}/pkgconfig/tss2-tcti-swtpm.pc
%{_mandir}/man3/*.3.gz
%{_mandir}/man5/*.5.gz
%{_mandir}/man7/tss2*.7.gz

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.3-9
- Prepare for Oreon 11 (RP1)
