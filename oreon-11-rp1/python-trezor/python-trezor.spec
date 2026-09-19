%global source0_hash none

Name:           python-trezor
Version:        0.20.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python library for communicating with Trezor Hardware Wallet

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-3.0-only
URL:            https://github.com/trezor/trezor-firmware/tree/main/python
Source:         %{pypi_source trezor}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'trezor' generated automatically by pyp2spec.}

Patch:          remove_click_upper_bound.patch

%description %_description

%package -n     python3-trezor
Summary:        %{summary}

%description -n python3-trezor %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-trezor ble,ethereum,extra,full,hidapi,qt-widgets,stellar


%prep
%autosetup -p1 -n trezor-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x ble,ethereum,extra,full,hidapi,qt-widgets,stellar


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-trezor -f %{pyproject_files}
%{_bindir}/trezorctl

%changelog
%autochangelog
