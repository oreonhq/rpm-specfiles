%global source0_hash none

Name:           python-url-normalize
Version:        3.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        URL normalization for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/niksite/url-normalize
Source:         %{pypi_source url_normalize}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'url-normalize' generated automatically by pyp2spec.}

Patch0:         https://github.com/niksite/url-normalize/pull/28.patch#/python-url-normalize-poetry-core.patch

%description %_description

%package -n     python3-url-normalize
Summary:        %{summary}

%description -n python3-url-normalize %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-url-normalize dev


%prep
%autosetup -p1 -n url_normalize-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-url-normalize -f %{pyproject_files}
%{_bindir}/url-normalize

%changelog
%autochangelog
