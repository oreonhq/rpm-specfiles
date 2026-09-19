%global source0_hash 3416030903d7635a5879ec5bbd2512f6fdb7f4d062f47f7a1347220c7ac800b9

%global srcname dict-sorted
%global modname sdict
%global eggname %(n=%{srcname}; echo ${n//-/.})

Name:           python-%{srcname}
Version:        1.0.0
Release:        37%{?dist}
Summary:        Dictionaries sorted by key or by comparison function

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/lukesneeringer/dict-sorted
Source0:        %{url}/archive/releases/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(six) >= 1.3

%description -n python3-%{srcname}
%{summary}.

Python 3 version.

%package doc
Summary:        Documentation for %{name}
BuildRequires:  %{_bindir}/sphinx-build

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-releases-%{version}

%build
%py3_build
sphinx-build -W -b html -d docs/_build/.doctrees/ docs/ docs/_build/html/

%install
%py3_install
rm -f docs/_build/html/.buildinfo

%check
%{__python3} test.py -v

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{eggname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%files doc
%license LICENSE
%doc docs/_build/html

%changelog
%autochangelog
