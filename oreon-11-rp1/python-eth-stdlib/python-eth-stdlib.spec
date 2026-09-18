%global source0_hash none

Name:           python-eth-stdlib
Version:        0.2.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Ethereum Standard Library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-3.0-only
URL:            https://github.com/skellet0r/eth-stdlib
Source:         %{pypi_source eth_stdlib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'eth-stdlib' generated automatically by pyp2spec.}

Patch:         python-eth-stdlib-0001-Switch-to-cryptodomex.patch
Patch:         python-eth-stdlib-0002-Clarify-licensing-terms.patch
Patch:         python-eth-stdlib-0003-Disable-pytest-coverage.patch
Patch:         python-eth-stdlib-0004-Fix-for-modern-poetry.patch

%description %_description

%package -n     python3-eth-stdlib
Summary:        %{summary}

%description -n python3-eth-stdlib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-eth-stdlib hypothesis


%prep
%autosetup -p1 -n eth_stdlib-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x hypothesis


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-eth-stdlib -f %{pyproject_files}

%changelog
%autochangelog
