%global source0_hash 5fd718c1e1d2270ace39225c4c8b8cecdf5fb29664fe361c0107a54a55bd500d
%global pypi_name colin
%{?python_enable_dependency_generator}
%bcond_without python3
Name:           %{pypi_name}
Version:        0.5.3
Release:        1%{?dist}
Summary:        Tool to check generic rules/best-practices for containers/images/dockerfiles.
License:        GPL-3.0-or-later
URL:            https://github.com/user-cont/colin
Source0:        https://files.pythonhosted.org/packages/source/c/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-%{pypi_name}
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
# /oreon:deps
%description
`colin` is a tool to check generic rules/best-practices
for containers/images/dockerfiles

%package -n     python3-%{pypi_name}
Summary:        Tool to check generic rules/best-practices for containers/images/dockerfiles.
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Recommends:     moby-engine
%description -n python3-%{pypi_name}
`colin` as a tool to check generic rules/best-practices
for containers/images/dockerfiles

%package doc
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
Summary:        colin documentation
%description doc
Documentation for colin

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build
PYTHONPATH="${PWD}:${PWD}/docs/" sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}
%install
%py3_install
%oreon_autofiles python3-colin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles colin-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-colin -f %{oreon_filedir}/python3-colin.list
%files -n colin-doc -f %{oreon_filedir}/colin-doc.list

%changelog

%autochangelog
