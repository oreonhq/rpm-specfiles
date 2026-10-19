%global source0_hash 7b35345da4fee8b7ad3e7ef93068aa43524db4e8a32671693695e8f6afde3023
%{?python_enable_dependency_generator}
%global py2support 0
%global srcname speg
%global commit 877acddfd5ac5ae8b4a4592d045e74e108477643
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           python-%{srcname}
Version:        0.3
Release:        1%{?dist}
Summary:        A PEG-based parser interpreter with memoization (in time)
License:        MIT
URL:            https://github.com/avakar/speg
Source0:        https://github.com/avakar/%{srcname}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
A PEG-based parser interpreter with memoization.

%package -n python3-%{srcname}
Summary:        A PEG-based parser interpreter with memoization (in time)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
A PEG-based parser interpreter with memoization.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-speg -f %{oreon_filedir}/python3-speg.list

%changelog

%autochangelog
