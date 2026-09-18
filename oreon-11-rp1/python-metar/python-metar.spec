%global source0_hash none

Name:           python-metar
Version:        2.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Metar - a package to parse METAR-coded weather reports

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/python-metar/python-metar/
Source:         %{pypi_source metar}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'metar' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-metar
Summary:        %{summary}

%description -n python3-metar %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-metar codecov,tests,typing


%prep
%autosetup -p1 -n metar-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x codecov,tests,typing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-metar -f %{pyproject_files}

%changelog
%autochangelog
