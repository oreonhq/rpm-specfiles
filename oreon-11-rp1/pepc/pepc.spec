%global source0_hash 54cb216e7d9ff5bf71028deee3a068d2cd7baaa3ceb5abc66b096d49a566cc70
Name:		pepc
Version:	2.0.5
Release:        1%{?dist}
Summary:        Power, Energy, and Performance Configurator
License:	BSD-3-Clause
Url:		https://github.com/intel/pepc
Source0:        https://github.com/intel/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		pyproject.patch
BuildArch:	noarch
Requires:	python3-pepc = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pepc = %{version}-%{release}
# /oreon:deps
%description
Pepc stands for "Power, Energy, and Performance Configurator".
This is a command-line tool for configuring various Linux and Hardware 
power management features.

%package -n python3-%{name}
Summary:	Pepc Python libraries
%description -n python3-%{name}
Pepc Python libraries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pepc* usr/lib64/python3*/site-packages/pepc* usr/bin/*

%check

%pytest \
%ifnarch x86_64 %{ix86}
  -k 'test_cpuinfo_get' \
%endif
  -v
%files
%files -n python3-pepc -f %{oreon_filedir}/python3-pepc.list

%changelog

%autochangelog
