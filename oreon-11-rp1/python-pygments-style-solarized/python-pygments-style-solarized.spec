%global source0_hash 4867d8903d8d065c42ed37219eb5e13a6e091f11f1b3cd4f9fab016ec737b97a
%global srcname pygments-style-solarized
%global sum Solarized style plugin for Pygments
Name:           python-%{srcname}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Solarized style plugin for Pygments
License:        MIT
URL:            https://github.com/shkumagai/pygments-style-solarized
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{sum}

%package -n     python3-%{srcname}
Summary:        %{sum}
Requires:       python3-pygments >= 1.5
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
%{sum}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pygments-style-solarized -f %{oreon_filedir}/python3-pygments-style-solarized.list

%changelog

%autochangelog
