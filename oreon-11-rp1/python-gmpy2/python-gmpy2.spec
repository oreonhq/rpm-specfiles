%global source0_hash none

Name:           python-gmpy2
Version:        2.3.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        gmpy2 interface to GMP, MPFR, and MPC for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-3.0-or-later
URL:            https://github.com/gmpy2/gmpy2
Source:         %{pypi_source gmpy2}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'gmpy2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-gmpy2
Summary:        %{summary}

%description -n python3-gmpy2 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-gmpy2 docs,tests


%prep
%autosetup -p1 -n gmpy2-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-gmpy2 -f %{pyproject_files}

%changelog
%autochangelog
