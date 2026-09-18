%global source0_hash none

Name:           python-contextily
Version:        1.7.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Context geo-tiles in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/geopandas/contextily
Source:         %{pypi_source contextily}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'contextily' generated automatically by pyp2spec.}

Patch:          0001-Mark-another-test-as-using-the-network.patch

%description %_description

%package -n     python3-contextily
Summary:        %{summary}

%description -n python3-contextily %_description


%prep
%autosetup -p1 -n contextily-%{version}


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


%files -n python3-contextily -f %{pyproject_files}

%changelog
%autochangelog
