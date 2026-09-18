%global source0_hash none

Name:           python-elementpath
Version:        5.1.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/sissaschool/elementpath
Source:         %{pypi_source elementpath}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'elementpath' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-elementpath
Summary:        %{summary}

%description -n python3-elementpath %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-elementpath dev,docs


%prep
%autosetup -p1 -n elementpath-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-elementpath -f %{pyproject_files}

%changelog
%autochangelog
