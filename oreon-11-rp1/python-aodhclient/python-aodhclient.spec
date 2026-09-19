%global source0_hash none

Name:           python-aodhclient
Version:        3.12.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python client library for Aodh

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://docs.openstack.org/python-aodhclient
Source:         %{pypi_source aodhclient}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aodhclient' generated automatically by pyp2spec.}

Patch0:           0001-Revert-Add-OSprofiler-support-for-Aodh-client.patch

%description %_description

%package -n     python3-aodhclient
Summary:        %{summary}

%description -n python3-aodhclient %_description


%prep
%autosetup -p1 -n aodhclient-%{version}


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


%files -n python3-aodhclient -f %{pyproject_files}
%{_bindir}/aodh

%changelog
%autochangelog
