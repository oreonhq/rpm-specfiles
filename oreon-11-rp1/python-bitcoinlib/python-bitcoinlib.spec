%global source0_hash 1da3e9f137d4d4708427483ba2bd51407c0e0c287545ec504a6e5bf471854ef7

# Created by pyp2rpm-3.2.2
%global pypi_name python-bitcoinlib
%global srcname bitcoinlib

Name:           python-%{srcname}
Version:        0.12.0
Release:        14%{?dist}
Summary:        The Swiss Army Knife of the Bitcoin protocol

License:        LGPL-3.0-or-later
URL:            https://github.com/petertodd/python-bitcoinlib
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
This Python 2/3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is lowlevel and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin works.

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
This Python 3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is lowlevel and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin works.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files bitcoin

%check
%{__python3} -m unittest discover

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc README.md

%changelog
%autochangelog
