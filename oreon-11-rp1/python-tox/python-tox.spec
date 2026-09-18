%global source0_hash none

Name:           python-tox
Version:        4.61.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        tox is a generic virtualenv management and test command line tool

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://tox.wiki
Source:         %{pypi_source tox}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tox' generated automatically by pyp2spec.}

Patch:          fix-tests.patch

%description %_description

%package -n     python3-tox
Summary:        %{summary}

%description -n python3-tox %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-tox completion,testing


%prep
%autosetup -p1 -n tox-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x completion,testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-tox -f %{pyproject_files}
%{_bindir}/tox

%changelog
%autochangelog
