%global source0_hash 818a7641068932ed6436d0af0a3bb77bbbde29df0a7142c8bd1a249e7c2f0d38
Name:           python-straight-plugin
Version:        1.5.0
Release:        1%{?dist}
Summary:        Python plugin loader
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ironfroggy/straight.plugin/
Source0:        https://files.pythonhosted.org/packages/48/89/34ae6a87784d0b607af61c84a52c313c598f1d86ce5c1e9eb6da038fee5f/straight.plugin-%{version}.tar.gz
Patch:          Remove-the-import-of-imp.find_module.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n     python3-straight-plugin
Summary:        Python plugin loader
%description -n python3-straight-plugin
straight.plugin is a Python plugin loader inspired by twisted.plugin with two
important distinctions:

 - Fewer dependencies
 - Python 3 compatible

The system is used to allow multiple Python packages to provide plugins within
a namespace package, where other packages will locate and utilize. The plugins
themselves are modules in a namespace package where the namespace identifies
the plugins in it for some particular purpose or intent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir straight.plugin-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-straight-plugin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-straight-plugin -f %{oreon_filedir}/python3-straight-plugin.list

%changelog

%autochangelog
