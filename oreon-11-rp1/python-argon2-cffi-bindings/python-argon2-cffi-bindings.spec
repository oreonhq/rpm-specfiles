%global source0_hash none

Name:           python-argon2-cffi-bindings
Version:        26.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Low-level CFFI bindings for Argon2

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/hynek/argon2-cffi-bindings
Source:         %{pypi_source argon2_cffi_bindings}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'argon2-cffi-bindings' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-argon2-cffi-bindings
Summary:        %{summary}

%description -n python3-argon2-cffi-bindings %_description


%prep
%autosetup -p1 -n argon2_cffi_bindings-%{version}


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


%files -n python3-argon2-cffi-bindings -f %{pyproject_files}

%changelog
%autochangelog
