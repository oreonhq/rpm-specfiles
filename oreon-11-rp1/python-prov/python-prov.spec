%global source0_hash a6dfd797acc400dd793c215eff01c49f599ee7a61dab173a5d2b537362a90c75

%{?python_enable_dependency_generator}

%global modname prov

Name:           python-%{modname}
Version:        2.0.0
Release:        14%{?dist}
Summary:        W3C Provenance Data Model supporting PROV-JSON and PROV-XML import/export

License:        MIT
URL:            https://pypi.python.org/pypi/prov
Source0:        https://github.com/trungdong/prov/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
A library for W3C Provenance Data Model supporting PROV-JSON and PROV-XML\
import/export.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{_bindir}/%{modname}-*
%{python3_sitelib}/%{modname}*

%changelog
%autochangelog
