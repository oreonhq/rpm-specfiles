%global source0_hash none

Name:           python-regex
Version:        2026.9.10
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Alternative regular expression module, to replace re.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0 AND CNRI-Python
URL:            https://github.com/mrabarnett/mrab-regex
Source:         %{pypi_source regex}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'regex' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-regex
Summary:        %{summary}

%description -n python3-regex %_description


%prep
%autosetup -p1 -n regex-%{version}


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


%files -n python3-regex -f %{pyproject_files}

%changelog
%autochangelog
