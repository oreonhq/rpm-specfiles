%global source0_hash none

Name:		test
Version:	1
Release:	1%{?dist}
Summary:	test
License:	None

%description
None

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
echo efi_alt_arch=%{efi_alt_arch}
echo efi_alt_arch_upper=%{efi_alt_arch_upper}
echo efi_arch=%{efi_arch}
echo efi_arch_upper=%{efi_arch_upper}
echo efi_esp_boot=%{efi_esp_boot}
echo efi_esp_dir=%{efi_esp_dir}
echo efi_esp_efi=%{efi_esp_efi}
echo efi_esp_root=%{efi_esp_root}
echo efi_has_alt_arch=%{efi_has_alt_arch}
echo efi_has_arch=%{efi_has_arch}
echo efi_srpm_macros_version=%{efi_srpm_macros_version}
echo efi_vendor=%{efi_vendor}
