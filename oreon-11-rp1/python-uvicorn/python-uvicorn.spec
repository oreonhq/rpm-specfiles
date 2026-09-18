%global source0_hash none

Name:           python-uvicorn
Version:        0.53.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The lightning-fast ASGI server.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://uvicorn.dev/
Source:         %{pypi_source uvicorn}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'uvicorn' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-uvicorn
Summary:        %{summary}

%description -n python3-uvicorn %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-uvicorn standard


%prep
%autosetup -p1 -n uvicorn-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x standard


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-uvicorn -f %{pyproject_files}
%{_bindir}/uvicorn

%changelog
%autochangelog
