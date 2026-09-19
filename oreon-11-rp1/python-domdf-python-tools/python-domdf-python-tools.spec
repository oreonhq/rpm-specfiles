%global source0_hash none

Name:           python-domdf-python-tools
Version:        3.10.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Helpful functions for Python 🐍 🛠️

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/domdfcoding/domdf_python_tools
Source:         %{pypi_source domdf_python_tools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'domdf-python-tools' generated automatically by pyp2spec.}

Patch:          Don-t-remove-egg-info-directory-in-setup.py.patch
Patch:          0001-tests-fix-pathlib.PurePosixPath-repr-on-py3.14.patch
Patch:          0002-words-fix-alphabet_sort-exception-handling-for-py3.1.patch

%description %_description

%package -n     python3-domdf-python-tools
Summary:        %{summary}

%description -n python3-domdf-python-tools %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-domdf-python-tools all,dates,testing


%prep
%autosetup -p1 -n domdf_python_tools-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,dates,testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-domdf-python-tools -f %{pyproject_files}

%changelog
%autochangelog
