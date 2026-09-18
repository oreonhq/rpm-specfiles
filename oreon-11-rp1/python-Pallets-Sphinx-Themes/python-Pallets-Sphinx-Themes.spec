%global source0_hash none

Name:           python-pallets-sphinx-themes
Version:        2.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx themes for Pallets and related projects.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/pallets/pallets-sphinx-themes/
Source:         %{pypi_source pallets_sphinx_themes}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pallets-sphinx-themes' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pallets-sphinx-themes
Summary:        %{summary}

%description -n python3-pallets-sphinx-themes %_description


%prep
%autosetup -p1 -n pallets_sphinx_themes-%{version}


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


%files -n python3-pallets-sphinx-themes -f %{pyproject_files}

%changelog
%autochangelog
