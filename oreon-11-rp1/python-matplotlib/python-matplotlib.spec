%global source0_hash none

Name:           python-matplotlib
Version:        3.11.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python plotting package

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        PSF-2.0
URL:            https://matplotlib.org
Source:         %{pypi_source matplotlib}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'matplotlib' generated automatically by pyp2spec.}

Patch1001:      0001-matplotlibrc-path-search-fix.patch
Patch1002:      0002-Set-FreeType-version-to-%{ftver}-and-update-tolerances.patch
Patch1003:      0003-Unpin-meson-python-build-requirement.patch
Patch0001:      0004-Use-old-stride_windows-implementation-on-32-bit-x86.patch
Patch0002:      0005-Partially-revert-TST-Fix-minor-issues-in-interactive.patch

%description %_description

%package -n     python3-matplotlib
Summary:        %{summary}

%description -n python3-matplotlib %_description


%prep
%autosetup -p1 -n matplotlib-%{version}


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


%files -n python3-matplotlib -f %{pyproject_files}

%changelog
%autochangelog
