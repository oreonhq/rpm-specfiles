%global source0_hash none

Name:           python-aiostream
Version:        0.8.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Generator-based operators for asynchronous iteration

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-3.0-or-later
URL:            https://github.com/vxgmichel/aiostream
Source:         %{pypi_source aiostream}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aiostream' generated automatically by pyp2spec.}

Patch0:         require-lower-setuptools-version.patch

%description %_description

%package -n     python3-aiostream
Summary:        %{summary}

%description -n python3-aiostream %_description


%prep
%autosetup -p1 -n aiostream-%{version}


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


%files -n python3-aiostream -f %{pyproject_files}

%changelog
%autochangelog
