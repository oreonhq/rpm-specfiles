%global source0_hash none

Name:           python-postorius
Version:        1.3.13
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A web user interface for GNU Mailman

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://gitlab.com/mailman/postorius
Source:         %{pypi_source postorius}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'postorius' generated automatically by pyp2spec.}

Patch:          postorius-dont-ship-examples.diff
Patch:          postorius-django52.diff

%description %_description

%package -n     python3-postorius
Summary:        %{summary}

%description -n python3-postorius %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-postorius test


%prep
%autosetup -p1 -n postorius-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-postorius -f %{pyproject_files}

%changelog
%autochangelog
