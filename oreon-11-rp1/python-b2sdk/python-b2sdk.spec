%global source0_hash none

Name:           python-b2sdk
Version:        2.13.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Backblaze B2 SDK

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Backblaze/b2-sdk-python
Source:         %{pypi_source b2sdk}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'b2sdk' generated automatically by pyp2spec.}

Patch0:         relax-setuptools_scm-version.patch

%description %_description

%package -n     python3-b2sdk
Summary:        %{summary}

%description -n python3-b2sdk %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-b2sdk full


%prep
%autosetup -p1 -n b2sdk-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x full


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-b2sdk -f %{pyproject_files}

%changelog
%autochangelog
