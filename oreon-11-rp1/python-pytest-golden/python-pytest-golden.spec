%global source0_hash none

Name:           python-pytest-golden
Version:        1.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Plugin for pytest that offloads expected outputs to data files

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/oprypin/pytest-golden
Source:         %{pypi_source pytest_golden}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-golden' generated automatically by pyp2spec.}

Patch:          https://github.com/oprypin/pytest-golden/pull/8.patch#/pytest-golden-drop-atomicwrites.patch

%description %_description

%package -n     python3-pytest-golden
Summary:        %{summary}

%description -n python3-pytest-golden %_description


%prep
%autosetup -p1 -n pytest_golden-%{version}


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


%files -n python3-pytest-golden -f %{pyproject_files}

%changelog
%autochangelog
