%global source0_hash none

Name:           python-requirements-parser
Version:        0.13.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        This is a small Python module for parsing Pip requirement files.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/madpah/requirements-parser/#readme
Source:         %{pypi_source requirements_parser}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'requirements-parser' generated automatically by pyp2spec.}

Patch:          pyproject.toml-limit-documentation-to-the-sdist.patch

%description %_description

%package -n     python3-requirements-parser
Summary:        %{summary}

%description -n python3-requirements-parser %_description


%prep
%autosetup -p1 -n requirements_parser-%{version}


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


%files -n python3-requirements-parser -f %{pyproject_files}

%changelog
%autochangelog
