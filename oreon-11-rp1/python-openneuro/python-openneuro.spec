%global source0_hash none

Name:           python-openneuro-py
Version:        2026.7.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python client for OpenNeuro.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-3.0-only
URL:            https://github.com/openneuro-py/openneuro-py
Source:         %{pypi_source openneuro_py}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'openneuro-py' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-openneuro-py
Summary:        %{summary}

%description -n python3-openneuro-py %_description


%prep
%autosetup -p1 -n openneuro_py-%{version}


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


%files -n python3-openneuro-py -f %{pyproject_files}
%{_bindir}/openneuro-py

%changelog
%autochangelog
