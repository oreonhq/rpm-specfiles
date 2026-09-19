%global source0_hash none

Name:           python-fakeredis
Version:        2.38.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python implementation of redis API, can be used for testing purposes.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/cunla/fakeredis-py
Source:         %{pypi_source fakeredis}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fakeredis' generated automatically by pyp2spec.}

Patch:          patch-script-mixing-to-use-luaruntime-directly.diff

%description %_description

%package -n     python3-fakeredis
Summary:        %{summary}

%description -n python3-fakeredis %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fakeredis bf,cf,json,lua,probabilistic,valkey,vectorset


%prep
%autosetup -p1 -n fakeredis-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x bf,cf,json,lua,probabilistic,valkey,vectorset


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fakeredis -f %{pyproject_files}

%changelog
%autochangelog
