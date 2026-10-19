%global source0_hash 76fc8fd7c24311e0ca2199a9e4db2156585acd7652a5cead98b07ef4f70f9b78
%global srcname sphinx_selective_exclude
%bcond_with tests
Name:           python-%{srcname}
Version:        1.0.3
Release:        1%{?dist}
Summary:        Sphinx eager ".. only::" directive and other selective rendition extensions
License:        LicenseRef-Callaway-BSD
Url:            https://github.com/pfalcon/sphinx_selective_exclude
Source0:        https://files.pythonhosted.org/packages/source/p/python-sphinx_selective_exclude/python-sphinx_selective_exclude-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Sphinx eager ".. only::" directive and other selective rendition extensions
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
Requires:       python3-sphinx
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-sphinx_selective_exclude -f %{oreon_filedir}/python3-sphinx_selective_exclude.list

%changelog

%autochangelog
