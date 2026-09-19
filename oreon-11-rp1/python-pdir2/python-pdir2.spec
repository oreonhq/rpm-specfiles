%global source0_hash none

Name:           python-pdir2
Version:        1.1.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pretty dir printing with joy

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/laike9m/pdir2
Source:         %{pypi_source pdir2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pdir2' generated automatically by pyp2spec.}

Patch0:         python313.patch

%description %_description

%package -n     python3-pdir2
Summary:        %{summary}

%description -n python3-pdir2 %_description


%prep
%autosetup -p1 -n pdir2-%{version}


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


%files -n python3-pdir2 -f %{pyproject_files}

%changelog
%autochangelog
