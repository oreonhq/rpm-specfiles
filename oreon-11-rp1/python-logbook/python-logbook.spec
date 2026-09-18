%global source0_hash none

Name:           python-logbook
Version:        1.10.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A logging replacement for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/getlogbook/logbook
Source:         %{pypi_source logbook}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'logbook' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-logbook
Summary:        %{summary}

%description -n python3-logbook %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-logbook all,brotli,compression,execnet,jinja,nteventlog,redis,sqlalchemy,zmq


%prep
%autosetup -p1 -n logbook-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,brotli,compression,execnet,jinja,nteventlog,redis,sqlalchemy,zmq


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-logbook -f %{pyproject_files}

%changelog
%autochangelog
