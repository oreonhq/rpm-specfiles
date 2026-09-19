%global source0_hash none

Name:           python-pyobd
Version:        0.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        BYMA Market Data Library - Open Data API client

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/franco-lamas/PyOBD
Source:         %{pypi_source pyobd}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyobd' generated automatically by pyp2spec.}

Patch0:         python-pyobd-0.9.3-pyobd-module.patch
Patch1:         python-pyobd-0.9.3-invalid-device-traceback-fix.patch
Patch2:         python-pyobd-0.9.3-configure-dialog-traceback-fix.patch
Patch3:         python-pyobd-0.9.3-python3.patch

%description %_description

%package -n     python3-pyobd
Summary:        %{summary}

%description -n python3-pyobd %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pyobd dev


%prep
%autosetup -p1 -n pyobd-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pyobd -f %{pyproject_files}

%changelog
%autochangelog
