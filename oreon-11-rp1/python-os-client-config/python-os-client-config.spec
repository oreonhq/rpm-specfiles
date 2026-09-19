%global source0_hash none

Name:           python-os-client-config
Version:        2.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OpenStack Client Configuation Library

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://docs.openstack.org/os-client-config/latest
Source:         %{pypi_source os_client_config}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'os-client-config' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-os-client-config
Summary:        %{summary}

%description -n python3-os-client-config %_description


%prep
%autosetup -p1 -n os_client_config-%{version}


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


%files -n python3-os-client-config -f %{pyproject_files}

%changelog
%autochangelog
