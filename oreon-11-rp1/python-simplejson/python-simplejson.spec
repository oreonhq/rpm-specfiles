%global source0_hash none

Name:           python-simplejson
Version:        4.1.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Simple, fast, extensible JSON encoder/decoder for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT OR AFL-2.1
URL:            https://github.com/simplejson/simplejson
Source:         %{pypi_source simplejson}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'simplejson' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-simplejson
Summary:        %{summary}

%description -n python3-simplejson %_description


%prep
%autosetup -p1 -n simplejson-%{version}


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


%files -n python3-simplejson -f %{pyproject_files}

%changelog
%autochangelog
