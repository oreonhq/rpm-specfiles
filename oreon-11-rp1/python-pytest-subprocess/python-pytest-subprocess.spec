%global source0_hash none

Name:           python-pytest-subprocess
Version:        1.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A plugin to fake subprocess for pytest

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/aklajnert/pytest-subprocess
Source:         %{pypi_source pytest_subprocess}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-subprocess' generated automatically by pyp2spec.}

Patch:          https://github.com/aklajnert/pytest-subprocess/commit/be30d9a94ba45afb600717e3fcd95b8b2ff2c60e.patch

%description %_description

%package -n     python3-pytest-subprocess
Summary:        %{summary}

%description -n python3-pytest-subprocess %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pytest-subprocess dev,docs,test


%prep
%autosetup -p1 -n pytest_subprocess-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pytest-subprocess -f %{pyproject_files}

%changelog
%autochangelog
