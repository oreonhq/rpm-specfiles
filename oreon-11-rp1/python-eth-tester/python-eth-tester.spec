%global source0_hash none

Name:           python-eth-tester
Version:        0.14.0~b1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        eth-tester: Tools for testing Ethereum applications.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/ApeWorX/eth-tester
Source:         %{pypi_source eth_tester 0.14.0b1}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'eth-tester' generated automatically by pyp2spec.}

Patch1:        python-eth-tester-0001-Relax-deps.patch
Patch2:        python-eth-tester-0002-Revert-bump-towncrier-version-pins.patch

%description %_description

%package -n     python3-eth-tester
Summary:        %{summary}

%description -n python3-eth-tester %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-eth-tester py-evm,pyevm


%prep
%autosetup -p1 -n eth_tester-0.14.0b1


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x py-evm,pyevm


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-eth-tester -f %{pyproject_files}

%changelog
%autochangelog
