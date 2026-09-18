%global source0_hash none

Name:           python-bcrypt
Version:        5.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Modern password hashing for your software and your servers

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/pyca/bcrypt/
Source:         %{pypi_source bcrypt}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'bcrypt' generated automatically by pyp2spec.}

Patch:          python-bcrypt-4.3.0-pyo3.patch

%description %_description

%package -n     python3-bcrypt
Summary:        %{summary}

%description -n python3-bcrypt %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-bcrypt tests,typecheck


%prep
%autosetup -p1 -n bcrypt-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x tests,typecheck


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-bcrypt -f %{pyproject_files}

%changelog
%autochangelog

