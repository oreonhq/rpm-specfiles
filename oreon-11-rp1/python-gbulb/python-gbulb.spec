%global source0_hash none

Name:           python-gbulb
Version:        0.6.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        GLib event loop for Python asyncio

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/beeware/gbulb
Source:         %{pypi_source gbulb}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'gbulb' generated automatically by pyp2spec.}

Patch:          requirements-versions.patch
Patch:          0001-Fix-compatibility-with-Python-3.13.patch

%description %_description

%package -n     python3-gbulb
Summary:        %{summary}

%description -n python3-gbulb %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-gbulb dev


%prep
%autosetup -p1 -n gbulb-%{version}


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


%files -n python3-gbulb -f %{pyproject_files}

%changelog
%autochangelog
