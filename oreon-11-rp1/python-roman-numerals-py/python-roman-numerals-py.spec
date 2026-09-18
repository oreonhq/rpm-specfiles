%global source0_hash none

Name:           python-roman-numerals-py
Version:        4.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        This package is deprecated, switch to roman-numerals.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        0BSD OR CC0-1.0
URL:            https://github.com/AA-Turner/roman-numerals/
Source:         %{pypi_source roman_numerals_py}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'roman-numerals-py' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-roman-numerals-py
Summary:        %{summary}

%description -n python3-roman-numerals-py %_description


%prep
%autosetup -p1 -n roman_numerals_py-%{version}


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


%files -n python3-roman-numerals-py -f %{pyproject_files}

%changelog
%autochangelog
