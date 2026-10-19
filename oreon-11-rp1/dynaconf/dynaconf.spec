%global source0_hash a08f6ab44025034ef3c9f86b32548ab01efd4039094a74bd9f028a43c63d016f
%global srcname dynaconf
%global common_desc \
Dynaconf is a layered configuration system for Python applications with strong \
support for 12-factor applications and extensions for Flask and Django
Name:           %{srcname}
Version:        3.3.5
Release:        1%{?dist}
Summary:        A dynamic configurator for python projects
License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source0:        https://files.pythonhosted.org/packages/source/d/dynaconf/dynaconf-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        A dynamic configurator for python projects
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
%{common_desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-dynaconf -f %{oreon_filedir}/python3-dynaconf.list

%changelog

%autochangelog
