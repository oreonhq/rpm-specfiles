%global source0_hash none

Name:           python-prefixed
Version:        0.9.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Prefixed alternative numeric library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MPL-2.0
URL:            https://prefixed.readthedocs.io
Source:         %{pypi_source prefixed}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'prefixed' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-prefixed
Summary:        %{summary}

%description -n python3-prefixed %_description


%prep
%autosetup -p1 -n prefixed-%{version}


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


%files -n python3-prefixed -f %{pyproject_files}

%changelog
%autochangelog
