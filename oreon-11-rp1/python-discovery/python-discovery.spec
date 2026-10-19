%global source0_hash cf87d3627dfb4412437fdd5b13eae402607722998d21567993aedbc59b23c15e
Name:           python-discovery
Version:        1.6.1
Release:        1%{?dist}
Summary:        Python discovery helper library
License:        MIT
URL:            https://pypi.org/project/python-discovery/
Source0:        https://files.pythonhosted.org/packages/source/p/python_discovery/python_discovery-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-vcs) >= 0.5
BuildRequires:  python3dist(hatchling) >= 1.27
BuildRequires:  python3dist(hatchling) >= 1.28
Requires:       python3-discovery = %{version}-%{release}
# /oreon:deps
%description
Python discovery helper library.

%package -n python3-python-discovery
Summary:        Python discovery helper library
%description -n python3-python-discovery
Python discovery helper library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir python_discovery-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-python-discovery usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%files
%files -n python3-python-discovery -f %{oreon_filedir}/python3-python-discovery.list

%changelog

%autochangelog
