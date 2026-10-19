%global source0_hash 2d3aaa9a85f2e35614860e07815bfe461c3c369fff932016440fac58d3ac5ff3
%{?python_enable_dependency_generator}
%global modname prov
Name:           python-%{modname}
Version:        3.2.1
Release:        1%{?dist}
Summary:        W3C Provenance Data Model supporting PROV-JSON and PROV-XML import/export
License:        MIT
URL:            https://pypi.python.org/pypi/prov
Source0:        https://github.com/trungdong/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-%{modname}
Summary:        W3C Provenance Data Model supporting PROV-JSON and PROV-XML import/export
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%description -n python3-%{modname}

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-prov -f %{oreon_filedir}/python3-prov.list

%changelog

%autochangelog
