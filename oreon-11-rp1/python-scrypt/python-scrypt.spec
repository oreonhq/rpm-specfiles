%global source0_hash none

Name:           python-scrypt
Version:        0.9.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Bindings for the scrypt key derivation function library

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/holgern/py-scrypt
Source:         %{pypi_source scrypt}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'scrypt' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-scrypt
Summary:        %{summary}

%description -n python3-scrypt %_description


%prep
%autosetup -p1 -n scrypt-%{version}


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


%files -n python3-scrypt -f %{pyproject_files}

%changelog
%autochangelog
