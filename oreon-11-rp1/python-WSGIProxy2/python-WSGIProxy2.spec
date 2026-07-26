%global source0_hash 60ee8da33b1736dd436d6f34cc733e397aed60fb7007eddd3db5197060e10111

%global pypi_name WSGIProxy2
%global package_name wsgiproxy

Name:           python-%{pypi_name}
Version:        0.4.6
Release:        25%{?dist}
Summary:        WSGI Proxy that supports several HTTP backends

License:        MIT
URL:            https://github.com/gawel/WSGIProxy2/
Source0:        https://pypi.python.org/packages/source/W/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%global _description\
WSGI Proxy that supports several HTTP backends.

%description %_description

%package -n     python3-%{pypi_name}
Summary:        WSGI Proxy that supports several HTTP backends
BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  python3-webtest
Requires:       python3-webob
Requires:       python3-six

%description -n python3-%{pypi_name} %_description

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{package_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README_fixt.py README.rst

%changelog
%autochangelog
