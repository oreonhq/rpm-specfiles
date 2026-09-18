%global source0_hash none

Name:           python-webscrapbook
Version:        2.10.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A backend toolkit for management of WebScrapBook collection.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/danny0838/PyWebScrapBook
Source:         %{pypi_source webscrapbook}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'webscrapbook' generated automatically by pyp2spec.}

Patch100:       python-webscrapbook-2.7.1-test-requirements.patch

%description %_description

%package -n     python3-webscrapbook
Summary:        %{summary}

%description -n python3-webscrapbook %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-webscrapbook adhoc-ssl


%prep
%autosetup -p1 -n webscrapbook-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x adhoc-ssl


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-webscrapbook -f %{pyproject_files}
%{_bindir}/webscrapbook
%{_bindir}/wsb
%{_bindir}/wsbview

%changelog
%autochangelog
