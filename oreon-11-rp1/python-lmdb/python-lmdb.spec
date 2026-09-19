%global source0_hash none

Name:           python-lmdb
Version:        2.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Universal Python binding for the LMDB _Lightning_ Database

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        OLDAP-2.8
URL:            http://github.com/jnwatson/py-lmdb/
Source:         %{pypi_source lmdb}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'lmdb' generated automatically by pyp2spec.}

Patch:          https://github.com/jnwatson/py-lmdb/pull/368.patch

%description %_description

%package -n     python3-lmdb
Summary:        %{summary}

%description -n python3-lmdb %_description


%prep
%autosetup -p1 -n lmdb-%{version}


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


%files -n python3-lmdb -f %{pyproject_files}

%changelog
%autochangelog
