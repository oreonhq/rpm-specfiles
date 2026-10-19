%global source0_hash 233bb6599ff404f4fab751433f6c192a301b9fb1ecdc3403f6bcd81f2fde48b4
Name:    python-mako
Version: 1.4.3
Release:        1%{?dist}
Summary:        Mako template library for Python
License: MIT AND Python-2.0.1 AND BSD-3-Clause
URL:     https://www.makotemplates.org/
Source0:        https://github.com/sqlalchemy/mako/archive/rel_1_4_3.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-markupsafe
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-mako
Summary:        Mako template library for Python
Recommends: python3-beaker
Obsoletes: python2-mako < 1.1.0-3
Obsoletes: python-mako-doc < 1.1.4-6
%{?python_provide:%python_provide python3-mako}
%description -n python3-mako

This package contains the mako module built for use with python3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n mako-rel_%(echo %{version} | sed "s/\./_/g")

# the package ends up installed as %%{version}.dev0 otherwise:
sed -i '/tag_build = dev/d' setup.cfg

%build

%py3_build
%install
%py3_install
mv %{buildroot}/%{_bindir}/mako-render %{buildroot}/%{_bindir}/mako-render-%{python3_version}
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render-3
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render
%oreon_autofiles python3-mako usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pytest-3
%files -f %{oreon_filedir}/main.list
%files -n python3-mako -f %{oreon_filedir}/python3-mako.list

%changelog

%autochangelog
