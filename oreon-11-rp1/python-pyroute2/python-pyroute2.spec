%global source0_hash 54d226fc3ff2732f49bac9b26853c50c9d05be05a4d9daf09c7cf6d77301eff3

%global srcname pyroute2

%global _description \
PyRoute2 provides several levels of API to work with Netlink\
protocols, such as Generic Netlink, RTNL, TaskStats, NFNetlink,\
IPQ.

Name: python-%{srcname}
Version: 0.7.12
Release: %autorelease
Summary: Pure Python netlink library
License: GPL-2.0-or-later OR Apache-2.0
URL: https://github.com/svinota/%{srcname}

BuildArch: noarch
Source0: %{pypi_source pyroute2}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary: %{summary}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyroute2

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%{_bindir}/ss2
%{_bindir}/%{srcname}-cli
%{_bindir}/%{srcname}-dhcp-client
%{_bindir}/%{srcname}-test-platform
%doc README*
%license LICENSE.GPL-2.0-or-later LICENSE.Apache-2.0
%{python3_sitelib}/pr2modules

%changelog
%autochangelog
