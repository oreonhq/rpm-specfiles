%global source0_hash none

Name:           python-urllib3
Version:        2.8.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        HTTP library with thread-safe connection pooling, file post, and more.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/urllib3/urllib3/blob/main/CHANGES.rst
Source:         %{pypi_source urllib3}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'urllib3' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-urllib3
Summary:        %{summary}

%description -n python3-urllib3 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-urllib3 brotli,h2,socks,zstd


%prep
%autosetup -p1 -n urllib3-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x brotli,h2,socks,zstd


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-urllib3 -f %{pyproject_files}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.0-1
- Import
