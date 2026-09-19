%global source0_hash none

Name:           python-etcd3gw
Version:        2.7.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python client for etcd3 grpc-gateway v3 API

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://docs.openstack.org/etcd3gw
Source:         %{pypi_source etcd3gw}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'etcd3gw' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-etcd3gw
Summary:        %{summary}

%description -n python3-etcd3gw %_description


%prep
%autosetup -p1 -n etcd3gw-%{version}


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


%files -n python3-etcd3gw -f %{pyproject_files}

%changelog
%autochangelog
