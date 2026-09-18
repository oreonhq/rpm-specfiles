%global source0_hash none

Name:           python-pydantic-core
Version:        2.49.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Core functionality for Pydantic validation and serialization

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pydantic
Source:         %{pypi_source pydantic_core}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pydantic-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pydantic-core
Summary:        %{summary}

%description -n python3-pydantic-core %_description


%prep
%autosetup -p1 -n pydantic_core-%{version}


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


%files -n python3-pydantic-core -f %{pyproject_files}

%changelog
%autochangelog
