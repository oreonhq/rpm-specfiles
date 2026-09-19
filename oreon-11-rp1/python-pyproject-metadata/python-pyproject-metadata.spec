%global source0_hash none

Name:           python-pyproject-metadata
Version:        0.12.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        PEP 621 metadata parsing

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/pyproject-metadata
Source:         %{pypi_source pyproject_metadata}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyproject-metadata' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyproject-metadata
Summary:        %{summary}

%description -n python3-pyproject-metadata %_description


%prep
%autosetup -p1 -n pyproject_metadata-%{version}


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


%files -n python3-pyproject-metadata -f %{pyproject_files}

%changelog
%autochangelog
