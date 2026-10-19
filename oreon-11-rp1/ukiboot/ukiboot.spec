%global source0_hash 018e56875c66e2b29c03aadee30baa1fd015b4f7172bc1ba7cdfb0ccde85ebc0
Name:		ukiboot
Version:	0.2.1
Release:        1%{?dist}
Summary:        A UEFI bootloader implementing UEFI based A/B boot
License:	LGPL-2.1-or-later
URL:		https://gitlab.com/CentOS/automotive/src/ukiboot
Source0:        https://gitlab.com/CentOS/automotive/src/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Requires:	efi-filesystem
ExclusiveArch:	%{efi}
# oreon:deps
BuildRequires:  efi-srpm-macros
BuildRequires:  gcc
BuildRequires:  gnu-efi-devel
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  systemd
BuildRequires:  systemd-boot
BuildRequires:  systemd-ukify
# /oreon:deps
%description
A UEFI bootloader implementing UEFI based A/B boot similar to
android boot.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -D esp-dir=EFI/%{efi_vendor}
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{efi_esp_dir}/ukiboot_a.efi.extra.d
mkdir -p %{buildroot}%{efi_esp_dir}/ukiboot_b.efi.extra.d
install %{buildroot}%{_libexecdir}/ukiboot/efi/ukiboot*.efi %{buildroot}%{efi_esp_dir}/
install %{buildroot}%{_libexecdir}/ukiboot/efi/slot_a.addon.efi %{buildroot}%{efi_esp_dir}/ukiboot_a.efi.extra.d
install %{buildroot}%{_libexecdir}/ukiboot/efi/slot_b.addon.efi %{buildroot}%{efi_esp_dir}/ukiboot_b.efi.extra.d
%oreon_autofiles main

%post

%systemd_post ukiboot-set-success.service
%preun

%systemd_preun ukiboot-set-success.service
%postun

%systemd_postun ukiboot-set-success.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
