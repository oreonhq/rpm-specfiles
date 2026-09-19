%global source0_hash none

Name:           python-watchfiles
Version:        1.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Simple, modern and high performance file watching and code reload in python.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
Source:         %{pypi_source watchfiles}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'watchfiles' generated automatically by pyp2spec.}

Patch:          0001-Downstream-only-allow-a-slightly-older-pytest-to-sup.patch

%description %_description

%package -n     python3-watchfiles
Summary:        %{summary}

%description -n python3-watchfiles %_description


%prep
%autosetup -p1 -n watchfiles-%{version}


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


%files -n python3-watchfiles -f %{pyproject_files}
%{_bindir}/watchfiles

%changelog
%autochangelog
