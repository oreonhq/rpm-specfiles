%global source0_hash none

Name:           python-stone
Version:        3.5.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Stone is an interface description language _IDL_ for APIs.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/dropbox/stone
Source:         %{pypi_source stone}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'stone' generated automatically by pyp2spec.}

Patch:          0001-Remove-pytest-runner-setup.py-test-support.patch

%description %_description

%package -n     python3-stone
Summary:        %{summary}

%description -n python3-stone %_description


%prep
%autosetup -p1 -n stone-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-stone -f %{pyproject_files}
%{_bindir}/stone

%changelog
%autochangelog
