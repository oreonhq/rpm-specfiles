%global source0_hash c9f1f9b9b967ea50eb0b478f0d7693d6673d4cd76c8e7eb80c55fc44ec928925
%global debug_package %{nil}
Summary:        Firmware update EFI binaries
Name:      fwupd-efi
Version:   1.8
Release:        1%{?dist}
License:   LGPL-2.1-or-later
URL:       https://github.com/fwupd/fwupd-efi
Source0:        https://github.com/fwupd/%{name}/archive/refs/tags/%{version}.tar.gz#/fwupd-efi-1.8.tar.gz
ExclusiveArch: x86_64 aarch64
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnu-efi-devel
BuildRequires:  meson
BuildRequires:  pesign
BuildRequires:  python3-pefile
# /oreon:deps
%description
fwupd is a project to allow updating device firmware, and this package provides
the EFI binary that is used for updating using UpdateCapsule.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8-1
- Prepare for Oreon 11 (RP1)
