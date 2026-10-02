%global source0_hash a5758ad00f0e1bbd60dc5a579a50259bff2e267e8e925d485351bf2bc683a329

Name:           python-pycdlib
Version:        1.21.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pure python ISO manipulation library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-only
URL:            http://github.com/clalancette/pycdlib
Source:         %{pypi_source pycdlib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pycdlib' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pycdlib
Summary:        %{summary}

%description -n python3-pycdlib %_description


%prep
%autosetup -p1 -n pycdlib-%{version}


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


%files -n python3-pycdlib -f %{pyproject_files}

%changelog
%autochangelog
