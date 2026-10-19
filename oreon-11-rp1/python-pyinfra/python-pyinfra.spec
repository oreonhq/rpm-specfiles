%global source0_hash 802d22046eb84937ffd2aadb7dd192a3cc2b830b026f9878617349614076810f
Name:           python-pyinfra
Version:        3.10.0
Release:        1%{?dist}
Summary:        pyinfra automates/provisions/manages/deploys infrastructure.
License:        MIT
URL:            https://pyinfra.com
Source0:        https://files.pythonhosted.org/packages/source/p/pyinfra/pyinfra-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyinfra = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyinfra
Summary:        pyinfra automates/provisions/manages/deploys infrastructure.
# oreon:reqs
Requires:       python3dist(click) > 2
Requires:       python3dist(distro) < 2
Requires:       python3dist(distro) >= 1.6
Requires:       python3dist(gevent) >= 1.5
Requires:       python3dist(jinja2) < 4
Requires:       python3dist(jinja2) > 3
Requires:       python3dist(packaging) >= 16.1
Requires:       python3dist(paramiko) < 5
Requires:       python3dist(paramiko) >= 2.11
Requires:       python3dist(pydantic) < 3
Requires:       python3dist(pydantic) >= 2.11
Requires:       python3dist(python-dateutil) < 3
Requires:       python3dist(python-dateutil) > 2
Requires:       python3dist(typeguard) < 5
Requires:       python3dist(typeguard) >= 4
Requires:       python3dist(types-paramiko) < 5
Requires:       python3dist(types-paramiko) >= 2.7
# /oreon:reqs
%description -n python3-pyinfra

%prep
%global oreon_srcdir pyinfra-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyinfra usr/lib/python3*/site-packages/pyinfra* usr/lib64/python3*/site-packages/pyinfra* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyinfra* usr/lib64/python3*/site-packages/pyinfra* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyinfra -f %{oreon_filedir}/python3-pyinfra.list

%changelog

%autochangelog
