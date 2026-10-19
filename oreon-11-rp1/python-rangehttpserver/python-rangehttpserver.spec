%global source0_hash 7ec021ebe26e0849cc7efa40ce231c0d9cc46027d37a80d728b3854c2149bfb4
%global desc %{expand: \
SimpleHTTPServer with support for Range requests.}
Name:           python-rangehttpserver
Version:        1.4.0
Release:        1%{?dist}
Summary:        SimpleHTTPServer with support for Range requests
License:        Apache-2.0
URL:            https://github.com/danvk/RangeHTTPServer
Source0:        https://github.com/danvk/RangeHTTPServer/archive/%{version}/RangeHTTPServer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rangehttpserver = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python3-rangehttpserver
Summary:        SimpleHTTPServer with support for Range requests
Requires: python3dist(requests)
%description -n python3-rangehttpserver
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n RangeHTTPServer-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

chmod 0644 RangeHTTPServer/__init__.py RangeHTTPServer/__main__.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rangehttpserver usr/lib/python3*/site-packages/rangehttpserver* usr/lib64/python3*/site-packages/rangehttpserver* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rangehttpserver* usr/lib64/python3*/site-packages/rangehttpserver* usr/bin/*

%check

%{pytest}
%files
%files -n python3-rangehttpserver -f %{oreon_filedir}/python3-rangehttpserver.list

%changelog

%autochangelog
