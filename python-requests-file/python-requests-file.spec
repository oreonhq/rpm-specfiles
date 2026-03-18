%global srcname requests_file

Name:           python-requests-file
Version:        3.0.0
Release:        2%{?dist}
Summary:        Transport adapter for using file:// URLs with python-requests

License:        Apache-2.0
URL:            https://codeberg.org/dashea/requests-file
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Requests-File is a transport adapter for use with the Requests Python
library to allow local file system access via file:// URLs.}

%description %_description

%package -n python3-requests-file
Summary:        %{summary}

%description -n python3-requests-file %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files requests_file

%check
%{pytest}

%files -n python3-requests-file -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-2
- Prepare for Oreon 11 (RP1)
