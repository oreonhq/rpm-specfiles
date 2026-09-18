%global source0_hash none

Name:           python-ns1-python
Version:        0.29.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python SDK for the NS1 DNS platform

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/ns1/ns1-python
Source:         %{pypi_source ns1_python}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ns1-python' generated automatically by pyp2spec.}

Patch0001:      https://github.com/ns1/ns1-python/pull/75.patch#/0001-Fixup-compatibility-with-Python-3.10.patch

%description %_description

%package -n     python3-ns1-python
Summary:        %{summary}

%description -n python3-ns1-python %_description


%prep
%autosetup -p1 -n ns1_python-%{version}


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


%files -n python3-ns1-python -f %{pyproject_files}

%changelog
%autochangelog
