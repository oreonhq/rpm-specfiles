%global source0_hash none

Name:           python-kerberos
Version:        1.3.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Kerberos high-level interface

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/apple/ccs-pykerberos
Source:         %{pypi_source kerberos}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'kerberos' generated automatically by pyp2spec.}

Patch1:         PY_SSIZE_T_CLEAN.patch
Patch2:         include_unistd.patch

%description %_description

%package -n     python3-kerberos
Summary:        %{summary}

%description -n python3-kerberos %_description


%prep
%autosetup -p1 -n kerberos-%{version}


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


%files -n python3-kerberos -f %{pyproject_files}

%changelog
%autochangelog
