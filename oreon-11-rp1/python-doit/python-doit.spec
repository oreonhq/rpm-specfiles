%global source0_hash none

Name:           python-doit
Version:        0.37.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        doit - Automation Tool

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pydoit.org
Source:         %{pypi_source doit}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'doit' generated automatically by pyp2spec.}

Patch1:         python-doit_ignore_versions.patch

%description %_description

%package -n     python3-doit
Summary:        %{summary}

%description -n python3-doit %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-doit cloudpickle,toml


%prep
%autosetup -p1 -n doit-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cloudpickle,toml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-doit -f %{pyproject_files}
%{_bindir}/doit

%changelog
%autochangelog
