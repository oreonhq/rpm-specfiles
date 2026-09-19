%global source0_hash none

Name:           python-wsgiproxy2
Version:        0.5.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A WSGI Proxy with various http client backends

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/gawel/WSGIProxy2/
Source:         %{pypi_source WSGIProxy2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'wsgiproxy2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-wsgiproxy2
Summary:        %{summary}

%description -n python3-wsgiproxy2 %_description


%prep
%autosetup -p1 -n WSGIProxy2-%{version}


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


%files -n python3-wsgiproxy2 -f %{pyproject_files}

%changelog
%autochangelog
