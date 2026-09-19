%global source0_hash none

Name:           python-oslo-utils
Version:        10.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Oslo Utility library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.utils
Source:         %{pypi_source oslo_utils}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'oslo-utils' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-oslo-utils
Summary:        %{summary}

%description -n python3-oslo-utils %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-oslo-utils image-inspection


%prep
%autosetup -p1 -n oslo_utils-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x image-inspection


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-oslo-utils -f %{pyproject_files}

%changelog
%autochangelog
