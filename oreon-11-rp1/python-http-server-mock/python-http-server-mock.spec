%global source0_hash a53986042414bb95506e2b486e7ab27e6ea0889160cdff794b5004ee79313907
Name:           python-http-server-mock
Version:        1.7
Release:        1%{?dist}
Summary:        Python 3 library to mock a http server using Flask
License:        GPL-3.0-only
URL:            https://github.com/ezequielramos/http-server-mock
Source0:        https://files.pythonhosted.org/packages/source/h/http_server_mock/http_server_mock-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
http-server-mock is a HTTP Server Mock using Flask. You can use it to test
possible integrations with your application.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-http-server-mock = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-http-server-mock
Summary:        Python 3 library to mock a http server using Flask
%description -n python3-http-server-mock %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir http_server_mock-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-http-server-mock usr/lib/python3*/site-packages/http_server_mock* usr/lib64/python3*/site-packages/http_server_mock* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/http_server_mock* usr/lib64/python3*/site-packages/http_server_mock* usr/bin/*

%check

%pytest
%files
%files -n python3-http-server-mock -f %{oreon_filedir}/python3-http-server-mock.list

%changelog

%autochangelog
