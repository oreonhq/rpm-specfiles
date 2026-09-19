%global source0_hash none

Name:           python-questionary
Version:        2.1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python library to build pretty command line user prompts ⭐️

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/tmbo/questionary
Source:         %{pypi_source questionary}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'questionary' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-questionary
Summary:        %{summary}

%description -n python3-questionary %_description


%prep
%autosetup -p1 -n questionary-%{version}


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


%files -n python3-questionary -f %{pyproject_files}

%changelog
%autochangelog
