%global source0_hash none

Name:           python-coveralls
Version:        4.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Show coverage stats online via coveralls.io

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/TheKevJames/coveralls-python
Source:         %{pypi_source coveralls}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'coveralls' generated automatically by pyp2spec.}

Patch0001:      0001-pyproject.toml-Allow-building-with-python-3.13.patch
Patch0002:      0002-pyproject-Use-docopt-ng-on-Fedora.patch

%description %_description

%package -n     python3-coveralls
Summary:        %{summary}

%description -n python3-coveralls %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-coveralls yaml


%prep
%autosetup -p1 -n coveralls-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x yaml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-coveralls -f %{pyproject_files}
%{_bindir}/coveralls
%{_bindir}/python-coveralls

%changelog
%autochangelog
