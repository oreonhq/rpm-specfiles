%global source0_hash none

Name:           python-tiny-proxy
Version:        0.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Simple proxy server _SOCKS4_a_, SOCKS5_h_, HTTP CONNECT_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/romis2012/tiny-proxy
Source:         %{pypi_source tiny_proxy}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tiny-proxy' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-tiny-proxy
Summary:        %{summary}

%description -n python3-tiny-proxy %_description


%prep
%autosetup -p1 -n tiny_proxy-%{version}


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


%files -n python3-tiny-proxy -f %{pyproject_files}

%changelog
%autochangelog
