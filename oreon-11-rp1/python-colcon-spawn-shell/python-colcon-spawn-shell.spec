%global source0_hash caf6a42aa9407208cea22d4c5340f6379a23701bd19afd08527170ed78c8adec

%global srcname colcon-spawn-shell

Name:           python-%{srcname}
Version:        0.3.0
Release:        10%{?dist}
Summary:        Source colcon workspaces in a new shell

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-spawn-shell
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This is a colcon plugin to chain workspaces in new shells. It allows quickly
un-chaining workspaces by exiting the spawned shell.

The shell's prompt is edited to show the workspace order. The only supported
shell is bash.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.12.0
Requires:       python%{python3_pkgversion}-colcon-bash >= 0.3.0
%endif

%description -n python%{python3_pkgversion}-%{srcname}
This is a colcon plugin to chain workspaces in new shells. It allows quickly
un-chaining workspaces by exiting the spawned shell.

The shell's prompt is edited to show the workspace order. The only supported
shell is bash.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/colcon_spawn_shell/
%{python3_sitelib}/colcon_spawn_shell-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
