%global source0_hash none

Name:           python-boutdata
Version:        0.4.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python package for collecting BOUT++ data

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-3.0-or-later
URL:            https://github.com/boutproject/boutdata
Source:         %{pypi_source boutdata}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'boutdata' generated automatically by pyp2spec.}

Patch:          https://github.com/boutproject/boutdata/pull/126.patch
Patch:          https://github.com/boutproject/boutdata/pull/125.patch

%description %_description

%package -n     python3-boutdata
Summary:        %{summary}

%description -n python3-boutdata %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-boutdata docs,lint,tests


%prep
%autosetup -p1 -n boutdata-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,lint,tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-boutdata -f %{pyproject_files}
%{_bindir}/bout-squashoutput
%{_bindir}/bout-upgrader

%changelog
%autochangelog
