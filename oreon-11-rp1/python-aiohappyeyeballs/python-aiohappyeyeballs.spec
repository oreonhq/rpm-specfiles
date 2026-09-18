%global source0_hash none

Name:           python-aiohappyeyeballs
Version:        2.7.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Happy Eyeballs for asyncio

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        PSF-2.0
URL:            https://github.com/aio-libs/aiohappyeyeballs
Source:         %{pypi_source aiohappyeyeballs}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aiohappyeyeballs' generated automatically by pyp2spec.}

Patch:          0001-Downstream-only-remove-pytest-options-for-coverage-a.patch
Patch:          0001-chore-deps-dev-bump-pytest-asyncio-from-0.26.0-to-1..patch

%description %_description

%package -n     python3-aiohappyeyeballs
Summary:        %{summary}

%description -n python3-aiohappyeyeballs %_description


%prep
%autosetup -p1 -n aiohappyeyeballs-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-aiohappyeyeballs -f %{pyproject_files}

%changelog
%autochangelog
