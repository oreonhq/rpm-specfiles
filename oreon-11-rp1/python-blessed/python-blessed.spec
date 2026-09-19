%global source0_hash none

Name:           python-blessed
Version:        1.50.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Easy, practical library for making terminal apps, by providing an elegant, well-documented interface for Terminals.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jquast/blessed
Source:         %{pypi_source blessed}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'blessed' generated automatically by pyp2spec.}

Patch0:     el7_req_fixes.patch
Patch1:     el7_pytest_fixes.patch

%description %_description

%package -n     python3-blessed
Summary:        %{summary}

%description -n python3-blessed %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-blessed docs


%prep
%autosetup -p1 -n blessed-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-blessed -f %{pyproject_files}

%changelog
%autochangelog
