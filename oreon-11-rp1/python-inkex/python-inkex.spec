%global source0_hash none

Name:           python-inkex
Version:        1.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python extensions for Inkscape core, separated out from main repository.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://gitlab.com/inkscape/extensions
Source:         %{pypi_source inkex}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'inkex' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-inkex
Summary:        %{summary}

%description -n python3-inkex %_description


%prep
%autosetup -p1 -n inkex-%{version}


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


%files -n python3-inkex -f %{pyproject_files}

%changelog
%autochangelog
