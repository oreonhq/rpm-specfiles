%global source0_hash 482110d52f6e3af68380dc3d1f3adaa6f5608d07e5b733a053c42aff8236d09e

%global sum An httplib2 transport for google-auth
%global srcname google-auth-httplib2

Name:           google-auth-httplib2
Summary:        %{sum}
Version:        0.3.0
Release:        2%{?dist}

License:        Apache-2.0
URL:            https://github.com/googleapis/google-auth-library-python-httplib2
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description 
httplib has lots of problems such as lack of threadsafety and insecure usage
of TLS. Using it is highly discouraged. This library is intended to help
existing users of oauth2client migrate to google-auth.

%package -n python3-%{srcname}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-%{srcname}
Written by Google, this library provides a small, flexible, and powerful 
Python 3 client library for accessing Google APIs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n google-auth-library-python-httplib2-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files google_auth_httplib2

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE 
%doc README.rst

%changelog
%autochangelog
