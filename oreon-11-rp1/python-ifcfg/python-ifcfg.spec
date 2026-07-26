%global source0_hash bf3cfa02425ad7adc5322fe88d18cb665e6228337d775c0c9cac441d3315e900

%global srcname ifcfg

Name:           python-%{srcname}
Version:        0.21
Release:        25%{?dist}
Summary:        Python cross-platform network interface discovery (ifconfig/ipconfig/ip)

License:        BSD-3-Clause
URL:            https://github.com/ftao/%{name}
Source0:        https://github.com/ftao/%{name}/archive/releases/%{version}/%{name}-releases-%{version}.tar.gz

# Not yet submitted upstream
Patch0:         %{name}-0.21-drop-nose.patch
# Maintainers, please upstream
Patch1:         %{name}-rm-python-mock-usage.patch

BuildArch:      noarch

%description
Ifcfg is a cross-platform library for parsing ifconfig and ipconfig output in
Python. It is useful for pulling information such as IP, Netmask, MAC Address,
Hostname, etc.

A fallback to ip is included for newer Unix systems w/o ifconfig.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  iproute
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     (iproute or net-tools)
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Ifcfg is a cross-platform library for parsing ifconfig and ipconfig output in
Python. It is useful for pulling information such as IP, Netmask, MAC Address,
Hostname, etc.

A fallback to ip is included for newer Unix systems w/o ifconfig.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-releases-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest \
  --override-ini 'python_files=*_tests.py' \
  tests

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
