%global source0_hash none

Name:           python-ijson
Version:        3.5.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Iterative JSON parser with standard Python iterator interfaces

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause AND ISC
URL:            https://github.com/ICRAR/ijson
Source:         %{pypi_source ijson}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ijson' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ijson
Summary:        %{summary}

%description -n python3-ijson %_description


%prep
%autosetup -p1 -n ijson-%{version}


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


%files -n python3-ijson -f %{pyproject_files}

%changelog
%autochangelog
