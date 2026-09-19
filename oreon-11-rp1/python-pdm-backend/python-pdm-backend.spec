%global source0_hash none

Name:           python-pdm-backend
Version:        2.4.9
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The build backend used by PDM that supports latest packaging standards

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pdm-project/pdm-backend
Source:         %{pypi_source pdm_backend}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pdm-backend' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pdm-backend
Summary:        %{summary}

%description -n python3-pdm-backend %_description


%prep
%autosetup -p1 -n pdm_backend-%{version}


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


%files -n python3-pdm-backend -f %{pyproject_files}

%changelog
%autochangelog
