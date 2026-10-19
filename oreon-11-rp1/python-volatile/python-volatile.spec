%global source0_hash 88e8268a435ce311ad54704aa57b8888ce619503b08744c573909f5e6b439f5e
%global srcname volatile
Name:           python-%{srcname}
Version:        2.1.0
Release:        1%{?dist}
Summary:        A small extension for the tempfile module
License:        MIT
URL:            https://github.com/mbr/volatile
Source0:        https://github.com/mbr/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        A small extension for the tempfile module
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v
%files -f %{oreon_filedir}/main.list
%files -n python3-volatile -f %{oreon_filedir}/python3-volatile.list

%changelog

%autochangelog
