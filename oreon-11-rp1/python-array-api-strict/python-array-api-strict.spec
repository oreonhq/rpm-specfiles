%global source0_hash none

Name:           python-array-api-strict
Version:        2.6.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A strict, minimal implementation of the Python array API standard.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://data-apis.org/array-api-strict/
Source:         %{pypi_source array_api_strict}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'array-api-strict' generated automatically by pyp2spec.}

Patch:          Fix-test_iter-with-Python-3.14-beta-1.patch

%description %_description

%package -n     python3-array-api-strict
Summary:        %{summary}

%description -n python3-array-api-strict %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-array-api-strict test


%prep
%autosetup -p1 -n array_api_strict-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-array-api-strict -f %{pyproject_files}

%changelog
%autochangelog
