%global source0_hash none

Name:           python-enlighten
Version:        1.14.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Enlighten Progress Bar

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MPL-2.0
URL:            https://python-enlighten.readthedocs.io
Source:         %{pypi_source enlighten}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'enlighten' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-enlighten
Summary:        %{summary}

%description -n python3-enlighten %_description


%prep
%autosetup -p1 -n enlighten-%{version}


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


%files -n python3-enlighten -f %{pyproject_files}

%changelog
%autochangelog
