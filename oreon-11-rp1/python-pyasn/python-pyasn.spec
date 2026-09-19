%global source0_hash none

Name:           python-pyasn
Version:        1.6.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Offline IP address to Autonomous System Number lookup module.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/hadiasghari/pyasn
Source:         %{pypi_source pyasn}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyasn' generated automatically by pyp2spec.}

Patch:          %{url}/commit/1d64d6d2f20e0353b46fbf5b94f8bdea8f41e9ce.patch

%description %_description

%package -n     python3-pyasn
Summary:        %{summary}

%description -n python3-pyasn %_description


%prep
%autosetup -p1 -n pyasn-%{version}


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


%files -n python3-pyasn -f %{pyproject_files}

%changelog
%autochangelog
