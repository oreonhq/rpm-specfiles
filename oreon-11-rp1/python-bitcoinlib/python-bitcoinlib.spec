%global source0_hash 941847029413ca4ea3a87f4830f64925c5692cdb5dbead01816ef98a2c864873
%global pypi_name python-bitcoinlib
%global srcname bitcoinlib
Name:           python-%{srcname}
Version:        0.12.0
Release:        1%{?dist}
Summary:        The Swiss Army Knife of the Bitcoin protocol
License:        LGPL-3.0-or-later
URL:            https://github.com/petertodd/python-bitcoinlib
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bitcoinlib = %{version}-%{release}
# /oreon:deps
%description
This Python 2/3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is lowlevel and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin works.

%package -n     python3-%{srcname}
Summary:        The Swiss Army Knife of the Bitcoin protocol
%description -n python3-%{srcname}
This Python 3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is lowlevel and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin works.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/bitcoinlib* usr/lib64/python3*/site-packages/bitcoinlib* usr/bin/*

%check

%{__python3} -m unittest discover
%files
%files -n python3-bitcoinlib -f %{oreon_filedir}/python3-bitcoinlib.list

%changelog

%autochangelog
