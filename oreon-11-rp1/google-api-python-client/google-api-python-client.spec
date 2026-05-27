%global source0_hash 6d6105dc69809ad8344f0d85140c36c9fe96a985057eaea457db8710a7fc97e8

%global sum Google APIs Client Library for Python
%global srcname google-api-client

Name:           google-api-python-client
Summary:        %{sum}
Epoch:          2
Version:        2.192.0
Release:        %autorelease

License:        Apache-2.0
URL:            https://github.com/googleapis/google-api-python-client
Source0:        https://github.com/googleapis/google-api-python-client/archive/v2.192.0/google-api-python-client-2.192.0.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description 
Written by Google, this library provides a small, flexible, and powerful
Python client library for accessing Google APIs.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
Written by Google, this library provides a small, flexible, and powerful 
Python 3 client library for accessing Google APIs.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files googleapiclient apiclient

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.192.0-1
- Prepare for Oreon 11 (RP1)
