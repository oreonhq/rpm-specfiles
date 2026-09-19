%global source0_hash none

Name:           python-authlib
Version:        1.8.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The ultimate Python library in building OAuth and OpenID Connect servers and clients.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/authlib/authlib
Source:         %{pypi_source authlib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'authlib' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-authlib
Summary:        %{summary}

%description -n python3-authlib %_description


%prep
%autosetup -p1 -n authlib-%{version}


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


%files -n python3-authlib -f %{pyproject_files}

%changelog
%autochangelog
