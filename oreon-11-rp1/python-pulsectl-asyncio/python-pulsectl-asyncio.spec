%global source0_hash none

Name:           python-pulsectl-asyncio
Version:        1.3.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Asyncio frontend for the pulsectl Python bindings of libpulse

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/mhthies/pulsectl-asyncio
Source:         %{pypi_source pulsectl_asyncio}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pulsectl-asyncio' generated automatically by pyp2spec.}

Patch:          python-pulsectl-24.12.0.diff

%description %_description

%package -n     python3-pulsectl-asyncio
Summary:        %{summary}

%description -n python3-pulsectl-asyncio %_description


%prep
%autosetup -p1 -n pulsectl_asyncio-%{version}


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


%files -n python3-pulsectl-asyncio -f %{pyproject_files}

%changelog
%autochangelog
