%global source0_hash 6c66d9cd3c014a0351df2b733c630e7b79e75a3224c808e457049b74f622edbe
Name:           python-quart
Version:        0.23.1
Release:        1%{?dist}
Summary:        A Python ASGI web microframework with the same API as Flask
License:        MIT
URL:            https://github.com/pallets/quart
Source0:        https://github.com/pallets/quart/archive/%{version}/quart-%{version}.tar.gz
Source10:       quart.1
Source11:       quart-routes.1
Source12:       quart-run.1
Source13:       quart-shell.1
Patch:          0001-Downstream-only-patch-out-coverage-analysis.patch
BuildArch:      noarch
%global common_description %{expand:
Quart is an async Python web microframework. Using Quart you can,
  * render and serve HTML templates,
  * write (RESTful) JSON APIs,
  * serve WebSockets,
  * stream request and response data,
  * do pretty much anything over the HTTP or WebSocket protocols.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-quart = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-quart
Summary:        A Python ASGI web microframework with the same API as Flask
%description -n python3-quart %{common_description}

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'
%oreon_autofiles python3-quart usr/lib/python3*/site-packages/quart* usr/lib64/python3*/site-packages/quart* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/quart* usr/lib64/python3*/site-packages/quart* usr/bin/*

%prep
%oreon_prep
%build

%pyproject_wheel
%check

%pytest -v
%files
%files -n python3-quart -f %{oreon_filedir}/python3-quart.list

%changelog

%autochangelog
