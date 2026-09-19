%global source0_hash none

Name:           python-botocore
Version:        1.43.98
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Low-level, data-driven core of boto 3.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/boto/botocore
Source:         %{pypi_source botocore}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'botocore' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-botocore
Summary:        %{summary}

%description -n python3-botocore %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-botocore crt


%prep
%autosetup -p1 -n botocore-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x crt


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-botocore -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.42.70-1
- Prepare for Oreon 11 (RP1)
