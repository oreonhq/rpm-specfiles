%global source0_hash none

Name:           python-virt-firmware
Version:        26.9
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        tools for virtual machine firmware volumes

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://gitlab.com/kraxel/virt-firmware
Source:         %{pypi_source virt_firmware}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'virt-firmware' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-virt-firmware
Summary:        %{summary}

%description -n python3-virt-firmware %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-virt-firmware crc32c


%prep
%autosetup -p1 -n virt_firmware-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x crc32c


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-virt-firmware -f %{pyproject_files}
%{_bindir}/host-efi-vars
%{_bindir}/kernel-bootcfg
%{_bindir}/migrate-vars
%{_bindir}/pe-addsigs
%{_bindir}/pe-dumpinfo
%{_bindir}/pe-inspect
%{_bindir}/pe-listsigs
%{_bindir}/uefi-boot-menu
%{_bindir}/uki-addons
%{_bindir}/virt-cloud-boot
%{_bindir}/virt-cloud-fetch
%{_bindir}/virt-fw-dump
%{_bindir}/virt-fw-measure
%{_bindir}/virt-fw-sigdb
%{_bindir}/virt-fw-vars
%{_bindir}/virt-kvm-caps

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.2-1
- Prepare for Oreon 11 (RP1)
