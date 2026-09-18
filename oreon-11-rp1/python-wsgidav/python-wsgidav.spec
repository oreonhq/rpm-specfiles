%global source0_hash none

Name:           python-wsgidav
Version:        4.3.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Generic and extendable WebDAV server based on WSGI

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/mar10/wsgidav
Source:         %{pypi_source wsgidav}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'wsgidav' generated automatically by pyp2spec.}

Patch:         %{url}/commit/991a23f5f5f3f46232eacd96666e23c1b5e110b5.patch

%description %_description

%package -n     python3-wsgidav
Summary:        %{summary}

%description -n python3-wsgidav %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-wsgidav pam


%prep
%autosetup -p1 -n wsgidav-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x pam


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-wsgidav -f %{pyproject_files}
%{_bindir}/wsgidav

%changelog
%autochangelog
