%global source0_hash 7ec021ebe26e0849cc7efa40ce231c0d9cc46027d37a80d728b3854c2149bfb4

%global desc %{expand: \
SimpleHTTPServer with support for Range requests.}

Name:           python-rangehttpserver
Version:        1.4.0
Release:        %autorelease
Summary:        SimpleHTTPServer with support for Range requests

License:        Apache-2.0
URL:            https://github.com/danvk/RangeHTTPServer
Source0:        %{url}/archive/%{version}/RangeHTTPServer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(requests)

%description
%{desc}

%package -n python3-rangehttpserver
Summary: %{summary}

Requires: python3dist(requests)
%description -n python3-rangehttpserver
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n RangeHTTPServer-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

chmod 0644 RangeHTTPServer/__init__.py RangeHTTPServer/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l RangeHTTPServer

%check
%{pytest}

%files -n python3-rangehttpserver -f %{pyproject_files}
%doc README

%changelog
%autochangelog
