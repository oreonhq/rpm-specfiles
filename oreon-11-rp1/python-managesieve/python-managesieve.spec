%global source0_hash none

Name:           python-managesieve
Version:        0.8.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        RFC-5804 Manage Sieve client library for remotely managing Sieve scripts

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        PSF-2.0 AND GPL-3.0-only
URL:            https://gitlab.com/htgoebel/managesieve/
Source:         %{pypi_source managesieve}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'managesieve' generated automatically by pyp2spec.}

Patch:          fix_ssl_wrap_socket_error.patch

%description %_description

%package -n     python3-managesieve
Summary:        %{summary}

%description -n python3-managesieve %_description


%prep
%autosetup -p1 -n managesieve-%{version}


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


%files -n python3-managesieve -f %{pyproject_files}

%changelog
%autochangelog
