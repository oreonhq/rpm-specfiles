%global source0_hash none

Name:           python-mkapi
Version:        4.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        MkDocs plugin for automatic API documentation generation from Python docstrings

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/daizutabi/mkapi
Source:         %{pypi_source mkapi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mkapi' generated automatically by pyp2spec.}

Patch:          %{forgeurl}/commit/e0777398e7f5e285bf88fbd0b048f2eeb3d9ceaa.patch

%description %_description

%package -n     python3-mkapi
Summary:        %{summary}

%description -n python3-mkapi %_description


%prep
%autosetup -p1 -n mkapi-%{version}


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


%files -n python3-mkapi -f %{pyproject_files}

%changelog
%autochangelog
