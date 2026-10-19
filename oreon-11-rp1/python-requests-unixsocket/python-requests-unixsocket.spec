%global source0_hash 87953038ae42befb6efbdf504d6dda2554a0b0d13b65e42f7319793b5527a303
Name:           python-requests-unixsocket2
Version:        1.0.1
Release:        1%{?dist}
Summary:        Use requests to talk HTTP via a UNIX domain socket
License:        ISC
URL:            https://gitlab.com/thelabnyc/requests-unixsocket2
Source0:        https://files.pythonhosted.org/packages/source/r/requests_unixsocket2/requests_unixsocket2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-requests-unixsocket2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-requests-unixsocket2
Summary:        Use requests to talk HTTP via a UNIX domain socket
# oreon:reqs
Requires:       python3dist(requests) (>=2.32.3
Requires:       python3dist(requests) < 3)
Requires:       python3dist(urllib3) (>=2.4.0
Requires:       python3dist(urllib3) < 3.0)
# /oreon:reqs
%description -n python3-requests-unixsocket2

%prep
%global oreon_srcdir requests_unixsocket2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requests-unixsocket2 usr/lib/python3*/site-packages/requests_unixsocket2* usr/lib64/python3*/site-packages/requests_unixsocket2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requests_unixsocket2* usr/lib64/python3*/site-packages/requests_unixsocket2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-requests-unixsocket2 -f %{oreon_filedir}/python3-requests-unixsocket2.list

%changelog

%autochangelog
