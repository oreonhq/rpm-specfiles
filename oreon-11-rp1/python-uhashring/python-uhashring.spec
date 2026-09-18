%global source0_hash none

Name:           python-uhashring
Version:        2.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Full featured consistent hashing python library compatible with ketama.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/ultrabug/uhashring
Source:         %{pypi_source uhashring}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'uhashring' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-uhashring
Summary:        %{summary}

%description -n python3-uhashring %_description


%prep
%autosetup -p1 -n uhashring-%{version}


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


%files -n python3-uhashring -f %{pyproject_files}

%changelog
%autochangelog
