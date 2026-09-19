%global source0_hash none

Name:           python-requests-unixsocket2
Version:        1.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Use requests to talk HTTP via a UNIX domain socket

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC
URL:            https://gitlab.com/thelabnyc/requests-unixsocket2
Source:         %{pypi_source requests_unixsocket2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'requests-unixsocket2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-requests-unixsocket2
Summary:        %{summary}

%description -n python3-requests-unixsocket2 %_description


%prep
%autosetup -p1 -n requests_unixsocket2-%{version}


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


%files -n python3-requests-unixsocket2 -f %{pyproject_files}

%changelog
%autochangelog
