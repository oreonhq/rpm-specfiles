%global source0_hash 83079122c51f781a3be03dc6814be5da4715a02f7acadb1f27f85ad22b72e603

%global prj_name geopmpy
%global desc %{expand: \
The Global Extensible Open Power Manager (GEOPM) provides a framework to
explore power and energy optimizations on platforms with heterogeneous mixes
of computing hardware.

Users can monitor their system's energy and power consumption, and safely
optimize system hardware settings to achieve energy efficiency and/or
performance objectives.}

Name:		python-%{prj_name}
Version:	3.2.1
Release:	%autorelease
Summary:	Python bindings for libgeopm

License:	BSD-3-Clause
URL:		https://geopm.github.io
Source0:	https://github.com/geopm/geopm/archive/v%{version}/geopm-%{version}.tar.gz

ExclusiveArch:	x86_64

BuildRequires:	gcc
BuildRequires:	python3-cffi
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	python3-geopmdpy >= 3.2.1
BuildRequires:	python3-cycler
BuildRequires:	python3-pandas
BuildRequires:	python3-natsort
BuildRequires:	python3-tables
BuildRequires:	python3-pyyaml
BuildRequires:	libgeopm-devel >= 3.2.1
BuildRequires:	libgeopmd-devel >= 3.2.1
Requires:	python3-cycler
Requires:	python3-natsort
Requires:	python3-pandas
Requires:	python3-tables
Requires:	python3-pyyaml
Requires:	geopmd

%description
%{desc}

%package -n python3-%{prj_name}
Summary:        %{summary}

%description -n python3-%{prj_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n geopm-%{version}

pushd %{prj_name}
echo %{version} > %{prj_name}/VERSION
popd

%build
pushd %{prj_name}
%py3_build
popd

%install
pushd %{prj_name}
%py3_install
popd

%check
pushd %{prj_name}
%{python3} -m unittest discover -s test -p 'Test*.py' -v
popd

%files -n python3-%{prj_name}
%license LICENSE-BSD-3-Clause
%doc README.md
%{python3_sitearch}/_libgeopm_py_cffi.abi3.so
%{python3_sitearch}/%{prj_name}
%{python3_sitearch}/%{prj_name}-*.egg-info
%{_bindir}/geopmlaunch

%changelog
%autochangelog
