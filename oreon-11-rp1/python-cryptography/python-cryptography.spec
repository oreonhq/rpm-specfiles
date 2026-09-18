%global source0_hash none

Name:           python-cryptography
Version:        50.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/pyca/cryptography
Source:         %{pypi_source cryptography}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cryptography' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-cryptography
Summary:        %{summary}

%description -n python3-cryptography %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-cryptography ssh


%prep
%autosetup -p1 -n cryptography-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x ssh


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-cryptography -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 46.0.5-1
- Prepare for Oreon 11 (RP1)
