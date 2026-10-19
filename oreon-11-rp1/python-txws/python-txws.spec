%global source0_hash 7e91e570341756994ba6dd00bd1bb2329ad9966a77a17a7d6d5a904fb66f419d
%global srcname txWS
%global libname txws
%global eggname %{srcname}
%global pkgname %{libname}
%bcond_without tests
Name:             python-%{pkgname}
Version:          0.9.1
Release:        1%{?dist}
Summary:        Twisted WebSockets wrapper
License:          MIT
URL:              https://github.com/MostAwesomeDude/txWS
Source0:        https://github.com/MostAwesomeDude/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:           0001-Drop-vcversioner.patch
Patch1:           python-txws-python39.patch
BuildArch:        noarch
%global common_description %{expand:
txWS (pronounced "Twisted WebSockets") is a small, short, simple library
for adding WebSockets server support to your favorite Twisted applications.}
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(twisted)
# /oreon:deps
%description %{common_description}

%package -n python3-%{pkgname}
Summary:        Twisted WebSockets wrapper
BuildRequires:    python3-devel
BuildRequires:    %{py3_dist setuptools}
%if %{with tests}
BuildRequires:    %{py3_dist Twisted six}
%endif
%{?python_provide:%python_provide python3-%{pkgname}}
%description -n python3-%{pkgname} %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
PYTHONPATH=$(pwd) trial-3 tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-txws -f %{oreon_filedir}/python3-txws.list

%changelog

%autochangelog
