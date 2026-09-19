%global source0_hash none

Name:           python-pyjson5
Version:        2.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        JSON5 serializer and parser for Python 3 written in Cython.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT OR Apache-2.0
URL:            https://github.com/Kijewski/pyjson5
Source:         %{pypi_source pyjson5}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyjson5' generated automatically by pyp2spec.}

Patch0:         flags.patch

%description %_description

%package -n     python3-pyjson5
Summary:        %{summary}

%description -n python3-pyjson5 %_description


%prep
%autosetup -p1 -n pyjson5-%{version}


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


%files -n python3-pyjson5 -f %{pyproject_files}

%changelog
%autochangelog
