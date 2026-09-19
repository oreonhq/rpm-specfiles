%global source0_hash none

Name:           python-stevedore
Version:        5.9.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Manage dynamic plugins for Python applications

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://docs.openstack.org/stevedore
Source:         %{pypi_source stevedore}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'stevedore' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-stevedore
Summary:        %{summary}

%description -n python3-stevedore %_description


%prep
%autosetup -p1 -n stevedore-%{version}


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


%files -n python3-stevedore -f %{pyproject_files}

%changelog
%autochangelog
