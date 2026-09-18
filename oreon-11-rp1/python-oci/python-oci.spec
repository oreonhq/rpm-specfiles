%global source0_hash none

Name:           python-oci
Version:        2.186.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Oracle Cloud Infrastructure Python SDK

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://docs.oracle.com/en-us/iaas/tools/python/latest/index.html
Source:         %{pypi_source oci}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'oci' generated automatically by pyp2spec.}

Patch0:         https://patch-diff.githubusercontent.com/raw/oracle/oci-python-sdk/pull/253.patch

%description %_description

%package -n     python3-oci
Summary:        %{summary}

%description -n python3-oci %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-oci adk


%prep
%autosetup -p1 -n oci-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x adk


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-oci -f %{pyproject_files}

%changelog
%autochangelog
