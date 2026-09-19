%global source0_hash none

Name:           python-starlette
Version:        1.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The little ASGI library that shines.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/Kludex/starlette
Source:         %{pypi_source starlette}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'starlette' generated automatically by pyp2spec.}

Patch:          python-starlette-CVE-2026-48710.patch

%description %_description

%package -n     python3-starlette
Summary:        %{summary}

%description -n python3-starlette %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-starlette full


%prep
%autosetup -p1 -n starlette-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x full


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-starlette -f %{pyproject_files}

%changelog
%autochangelog
