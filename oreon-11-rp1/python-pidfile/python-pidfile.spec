%global source1_hash 884221e32924b309b2635d1ac877ad186e041326d437685ed2653edc92d72c63
%global source0_hash 1e1097df41bc75f574599ffef89e8b20eff1bdfc9191d3ed264cc2dae95429d0
%global module_name pidfile
%global pypi_name python-%{module_name}
Name:			%{pypi_name}
Version:		3.0.0
Release:        1%{?dist}
Summary:        Python context manager for managing pid files
License:		MIT
URL:			https://pypi.org/project/python-pidfile
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Source1:		https://raw.githubusercontent.com/mosquito/python-pidfile/master/LICENSE
BuildArch:		noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pidfile = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{module_name}
Summary:        Python context manager for managing pid files
BuildRequires:	python3-devel
%description -n python3-%{module_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup %{name}-%{version}
cp -p %{SOURCE1} .

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pidfile* usr/lib64/python3*/site-packages/pidfile* usr/bin/*

%check

%pyproject_check_import
%doc README.rst
%license LICENSE
%files
%files -n python3-pidfile -f %{oreon_filedir}/python3-pidfile.list

%changelog

%autochangelog
