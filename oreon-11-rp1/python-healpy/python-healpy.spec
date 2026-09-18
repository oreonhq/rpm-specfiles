%global source0_hash none

Name:           python-healpy
Version:        1.20.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Healpix tools package for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-only
URL:            https://github.com/healpy/healpy
Source:         %{pypi_source healpy}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'healpy' generated automatically by pyp2spec.}

Patch:          pykg-config_requirements.patch
Patch:          no_pytest-cython_doctests.patch

%description %_description

%package -n     python3-healpy
Summary:        %{summary}

%description -n python3-healpy %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-healpy all,doc,test


%prep
%autosetup -p1 -n healpy-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,doc,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-healpy -f %{pyproject_files}

%changelog
%autochangelog
