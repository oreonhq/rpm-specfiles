%global source0_hash none

Name:           python-oracledb
Version:        4.0.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python interface to Oracle Database

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        UPL-1.0 OR Apache-2.0
URL:            https://oracle.github.io/python-oracledb
Source:         %{pypi_source oracledb}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'oracledb' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-oracledb
Summary:        %{summary}

%description -n python3-oracledb %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-oracledb azure-auth,azure-config,oci-auth,oci-config,test


%prep
%autosetup -p1 -n oracledb-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x azure-auth,azure-config,oci-auth,oci-config,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-oracledb -f %{pyproject_files}

%changelog
%autochangelog
