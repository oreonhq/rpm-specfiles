%global source0_hash 4d5dd0d43307f6577d984af68beeb657281c57f44609342e71703050ac327a3c
Name:           python-kmod
License:        LGPL-2.0-or-later
Summary:        Python module to work with kernel modules
Version:        0.9.1
Release:        1%{?dist}
URL:            https://github.com/maurizio-lombardi/python-kmod/
Source0:        https://github.com/agrover/python-kmod/archive/refs/tags/v%{version}.tar.gz#/python-kmod-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  kmod-devel
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-kmod
Summary:        Python module to work with kernel modules
%description -n python3-kmod
Python module to allow listing, loading, and unloading
Linux kernel modules, using libkmod.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
sed -i '1i# cython: legacy_implicit_noexcept=True' kmod/module.pyx

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-kmod usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-kmod -f %{oreon_filedir}/python3-kmod.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.2-12
- Import
