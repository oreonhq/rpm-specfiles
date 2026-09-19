%global source0_hash none

Name:           python-gssapi
Version:        1.12.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python GSSAPI Wrapper

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC
URL:            https://github.com/pythongssapi/python-gssapi
Source:         %{pypi_source gssapi}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'gssapi' generated automatically by pyp2spec.}

Patch0:         cython3.patch

%description %_description

%package -n     python3-gssapi
Summary:        %{summary}

%description -n python3-gssapi %_description


%prep
%autosetup -p1 -n gssapi-%{version}


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


%files -n python3-gssapi -f %{pyproject_files}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.3-16
- Import
