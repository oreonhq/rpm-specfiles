%global source0_hash 3416030903d7635a5879ec5bbd2512f6fdb7f4d062f47f7a1347220c7ac800b9
%global srcname dict-sorted
%global modname sdict
%global eggname %(n=%{srcname}; echo ${n//-/.})
Name:           python-%{srcname}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Dictionaries sorted by key or by comparison function
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/lukesneeringer/dict-sorted
Source0:        https://github.com/lukesneeringer/%{srcname}/archive/releases/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  //bin/sphinx-build
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(six)
# /oreon:deps
%description
%{summary}.

%package -n python3-%{srcname}
Summary:        Dictionaries sorted by key or by comparison function
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} test.py -v
%files -f %{oreon_filedir}/main.list
%files -n python3-dict-sorted -f %{oreon_filedir}/python3-dict-sorted.list
%files -n python-dict-sorted-doc -f %{oreon_filedir}/python-dict-sorted-doc.list

%changelog

%autochangelog
