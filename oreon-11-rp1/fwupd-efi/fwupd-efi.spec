%global debug_package %{nil}

Summary:   Firmware update EFI binaries
Name:      fwupd-efi
Version:   1.8
Release:   %autorelease
License:   LGPL-2.1-or-later
URL:       https://github.com/fwupd/fwupd-efi
Source0:   https://github.com/fwupd/%{name}/archive/refs/tags/%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 c9f1f9b9b967ea50eb0b478f0d7693d6673d4cd76c8e7eb80c55fc44ec928925
%global source0_file 1.8.tar.gz
# oreon url source checksums end

# these are the only architectures supporting UEFI UpdateCapsule
ExclusiveArch: x86_64 aarch64

BuildRequires: gcc
BuildRequires: meson
BuildRequires: gnu-efi-devel >= 3.0.18
BuildRequires: pesign
BuildRequires: python3-pefile

%description
fwupd is a project to allow updating device firmware, and this package provides
the EFI binary that is used for updating using UpdateCapsule.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/1.8.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c9f1f9b9b967ea50eb0b478f0d7693d6673d4cd76c8e7eb80c55fc44ec928925" || { echo "oreon: Source0 SHA256 mismatch for 1.8.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build

%meson \
    -Dgenpeimg=disabled \
    -Defi_sbat_distro_id="fedora" \
    -Defi_sbat_distro_summary="The Fedora Project" \
    -Defi_sbat_distro_pkgname="%{name}" \
    -Defi_sbat_distro_version="%{version}-%{release}" \
    -Defi_sbat_distro_url="https://src.fedoraproject.org/rpms/%{name}"

%meson_build

%install
%meson_install

# sign fwupd.efi loader
%ifarch x86_64
%global efiarch x64
%endif
%ifarch aarch64
%global efiarch aa64
%endif
%global fwup_efi_fn $RPM_BUILD_ROOT%{_libexecdir}/fwupd/efi/fwupd%{efiarch}.efi
%pesign -s -i %{fwup_efi_fn} -o %{fwup_efi_fn}.tmp
%define __pesign_client_cert fwupd-signer
%pesign -s -i %{fwup_efi_fn}.tmp -o %{fwup_efi_fn}.signed
rm -vf %{fwup_efi_fn}.tmp

%files
%doc README.md AUTHORS
%license COPYING
%dir %{_libexecdir}/fwupd/efi
%{_libexecdir}/fwupd/efi/*.efi
%{_libexecdir}/fwupd/efi/*.efi.signed
%{_libdir}/pkgconfig/fwupd-efi.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8-1
- Prepare for Oreon 11 (RP1)
