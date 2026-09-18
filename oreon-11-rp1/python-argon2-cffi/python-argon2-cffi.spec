%global source0_hash none

Name:           python-argon2-cffi
Version:        25.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Argon2 for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/hynek/argon2-cffi
Source:         %{pypi_source argon2_cffi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'argon2-cffi' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-argon2-cffi
Summary:        %{summary}

%description -n python3-argon2-cffi %_description


%prep
%autosetup -p1 -n argon2_cffi-%{version}


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


%files -n python3-argon2-cffi -f %{pyproject_files}

%changelog
%autochangelog
