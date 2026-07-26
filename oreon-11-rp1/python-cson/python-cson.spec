%global source0_hash dd3b7d8f773219588867a33ca910999243aa941d2ec3c3b05bc4a26a590100f7

%{?python_enable_dependency_generator}
%global py2support 0
%global srcname cson

Name:           python-%{srcname}
Version:        0.8
Release:        26%{?dist}
Summary:        A Coffescript Object Notation (CSON) parser for Python 2 and Python 3
License:        MIT
URL:            https://github.com/avakar/pycson
Source0:        https://github.com/avakar/pycson/archive/%{version}/pycson-%{version}.tar.gz
BuildArch:      noarch

%description
A python parser for the Coffeescript Object Notation (CSON).

%if %{py2support}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A python parser for the Coffeescript Object Notation (CSON).
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A python parser for the Coffeescript Object Notation (CSON).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pycson-%{version}

%build
%if %{py2support}
%py2_build
%endif
%py3_build

%install
%if %{py2support}
%py2_install
%endif
%py3_install

# Note that there is no %%files section for the unversioned python module
%if %{py2support}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{srcname}/
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
