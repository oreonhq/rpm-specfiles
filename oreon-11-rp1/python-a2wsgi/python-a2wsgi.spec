%global source0_hash none

Name:           python-a2wsgi
Version:        1.10.10
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Convert WSGI app to ASGI app or ASGI app to WSGI app.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/abersheeran/a2wsgi
Source:         %{pypi_source a2wsgi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'a2wsgi' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-a2wsgi
Summary:        %{summary}

%description -n python3-a2wsgi %_description


%prep
%autosetup -p1 -n a2wsgi-%{version}


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


%files -n python3-a2wsgi -f %{pyproject_files}

%changelog
%autochangelog
