%global source0_hash none

Name:           python-ulid
Version:        4.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Universally unique lexicographically sortable identifier

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/mdomke/python-ulid
Source:         %{pypi_source python_ulid}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-ulid' generated automatically by pyp2spec.}

Patch:          0001-Depend-on-typing-extensions-for-Python-3.11-avoid-it.patch

%description %_description

%package -n     python3-python-ulid
Summary:        %{summary}

%description -n python3-python-ulid %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-python-ulid pydantic


%prep
%autosetup -p1 -n python_ulid-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x pydantic


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-python-ulid -f %{pyproject_files}
%{_bindir}/ulid

%changelog
%autochangelog
