# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0c74e146e96aa56c4ce832cf299e4ae38b80953cbdb9f47ae72ab85b1965cb9f
%global debug_package %{nil}

Name: efi-srpm-macros
Version: 6
Release: 1%{?dist}
Summary: SRPM macros for EFI packages
License: GPL-3.0-or-later
URL: https://github.com/rhboot/efi-rpm-macros
BuildArch: noarch
Source0: https://github.com/rhboot/efi-rpm-macros/archive/refs/tags/%{version}.tar.gz
Requires: rpm

BuildRequires: oreon-rpm-macros

%description
SRPM macros that describe the EFI system partition and vendor directory.

%prep
%autosetup -n efi-rpm-macros-%{version} -p1
%oreon_sha256

%build
for i in macros.efi-srpm brp-boot-efi-times; do
sed \
  -e 's,@@EFI_ESP_ROOT@@,/boot/efi,g' \
  -e 's,@@EFI_ARCHES@@,"x86_64 aarch64",g' \
  -e 's,@@EFI_VENDOR@@,oreon,g' \
  -e 's,@@EFI_RPM_MACROS_VERSION@@,%{version},g' \
  -e 's,@@EFI_PRERELEASE@@,,g' \
  -e 's,@@EFI_SOURCE_VERSION@@,%{version},g' \
  -e 's,@@RPM_CONFIG_DIR@@,%{_rpmconfigdir},g' \
  $i.in > $i
done

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}
install -m 644 macros.efi-srpm %{buildroot}%{_rpmmacrodir}/macros.efi-srpm
install -m 755 brp-boot-efi-times %{buildroot}%{_rpmconfigdir}/brp-boot-efi-times

%files
%license LICENSE
%{_rpmmacrodir}/macros.efi-srpm
%{_rpmconfigdir}/brp-boot-efi-times
