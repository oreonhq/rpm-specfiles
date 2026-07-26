%global source0_hash 75a76a81e64d2b4e70b48e5f9a4c5c5296d323066bfd9d53b799756c28abf9da

%global srcname cerealizer
%global sum Secure pickle-like module

Name:			python-%{srcname}
Summary: 		%{sum}
Version:		0.8.2
Release:		28%{?dist}
# Automatically converted from old format: Python - review is highly recommended.
License:		LicenseRef-Callaway-Python
Source0:		https://files.pythonhosted.org/packages/5a/2b/8a2ff505db0ef7ce59f700b96898369b22a823c8d9191eba37639e568667/Cerealizer-%{version}.tar.gz
URL:			http://www.lesfleursdunormal.fr/static/informatique/cerealizer/index_en.html
BuildArch:		noarch
BuildRequires:		python3-devel
BuildRequires:		python3-setuptools

%description
Cerealizer is a secure pickle-like module. It support basic types (int, string,
unicode, tuple, list, dict, set,...), old and new-style classes (you need to 
register the class for security), object cycles, and it can be extended to 
support C-defined type.

%package -n python3-%{srcname}
Summary:                %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Cerealizer is a secure pickle-like module. It support basic types (int, string,
unicode, tuple, list, dict, set,...), old and new-style classes (you need to 
register the class for security), object cycles, and it can be extended to 
support C-defined type.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cerealizer-%{version}

%build
/usr/bin/python3 ./setup.py build

%install
/usr/bin/python3 ./setup.py install --skip-build --root $RPM_BUILD_ROOT

%files -n python3-%{srcname}
%doc README.rst PKG-INFO
%{python3_sitelib}/*

%changelog
%autochangelog
