%global source0_hash d6f042dd46aba79c4e7302ff20ec17878c41a8543d167845a73c26a108c082d1
%global srcname templated-dictionary
%global python3_pkgversion 3
Name:       python-%{srcname}
Version:    1.6
Release:        1%{?dist}
Summary:        Dictionary with Jinja2 expansion
License:    GPL-2.0-or-later
URL:        https://github.com/xsuchy/templated-dictionary
Source0:        %{name}-%{version}.tar.gz
BuildArch: noarch
Requires:      python%{python3_pkgversion}-jinja2
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Dictionary with Jinja2 expansion
%{?py_provides:%py_provides python3-%{srcname}}
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

version="%version" %py3_build
%install
version=%version %py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-templated-dictionary -f %{oreon_filedir}/python3-templated-dictionary.list

%changelog

%autochangelog
