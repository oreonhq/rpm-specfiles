%global source0_hash none

Name:           python-werkzeug
Version:        3.1.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The comprehensive WSGI web application library.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/pallets/werkzeug/
Source:         %{pypi_source werkzeug}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'werkzeug' generated automatically by pyp2spec.}

Patch:          preserve-any-existing-PYTHONPATH-in-tests.patch

%description %_description

%package -n     python3-werkzeug
Summary:        %{summary}

%description -n python3-werkzeug %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-werkzeug watchdog


%prep
%autosetup -p1 -n werkzeug-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x watchdog


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-werkzeug -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.6-1
- Prepare for Oreon 11 (RP1)
