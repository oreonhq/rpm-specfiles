%global source0_hash none

Name:           python-syrupy
Version:        6.1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pytest Snapshot Test Utility

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/syrupy-project/syrupy
Source:         %{pypi_source syrupy}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'syrupy' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-syrupy
Summary:        %{summary}

%description -n python3-syrupy %_description


%prep
%autosetup -p1 -n syrupy-%{version}


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


%files -n python3-syrupy -f %{pyproject_files}

%changelog
%autochangelog
