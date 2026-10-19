%global source0_hash ad86be1fd4d545c3ef941ec89ef08875b486ccd0aa03b914f2849c874d471008
%global commit ca0ea3b56decaf6ee668e4ab32278499389ca35f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20240211
Name:           syndication-domination
Version:        1.0%{?gitdate:^%{gitdate}.git%{shortcommit}}
Release:        1%{?dist}
Summary:        A simple RSS/Atom parser library
License:        AGPL-3.0-or-later
URL:            https://gitlab.com/gabmus/syndication-domination
%if 0%{?gitdate}
Source0:        https://gitlab.com/gabmus/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
%else
%endif
Patch:          0001-Install-into-python.platlibdir.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(pybind11)
BuildRequires:  pkgconfig(tidy)
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11
# /oreon:deps
%description

%package -n python3-syndom
Summary:        A simple RSS/Atom parser library
%description -n python3-syndom

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 %{?gitdate:-n %{name}-%{commit}}

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles python3-syndom usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n python3-syndom -f %{oreon_filedir}/python3-syndom.list

%changelog

%autochangelog
