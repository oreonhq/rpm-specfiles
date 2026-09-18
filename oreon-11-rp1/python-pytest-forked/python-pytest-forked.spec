%global source0_hash none

Name:           python-pytest-forked
Version:        1.7.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        run tests in isolated forked subprocesses

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
Source:         %{pypi_source pytest_forked}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-forked' generated automatically by pyp2spec.}

Patch:          https://github.com/pytest-dev/pytest-forked/commit/b2742322d3.patch

%description %_description

%package -n     python3-pytest-forked
Summary:        %{summary}

%description -n python3-pytest-forked %_description


%prep
%autosetup -p1 -n pytest_forked-%{version}


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


%files -n python3-pytest-forked -f %{pyproject_files}

%changelog
%autochangelog
