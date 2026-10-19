%global source0_hash 15de008451739d29ecf8089f550f4c96c45ae06bc68e1e6821e267a5ef4ec176
%global pretty_name BatAlgorithm
%global extract_name buma-BatAlgorithm-d913e9d
%global new_name batalgorithm
Name:           python-%{new_name}
Version:        0.3.1
Release:        19%{?dist}
Summary:        Bat Algorithm for optimization
License:        MIT
URL:            https://github.com/buma/BatAlgorithm
Source0:        https://github.com/buma/%{pretty_name}/tarball/master/%{extract_name}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-%{new_name}
Summary:        Bat Algorithm for optimization
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%description -n python3-%{new_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{extract_name}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-batalgorithm -f %{oreon_filedir}/python3-batalgorithm.list

%changelog

%autochangelog
