%global source0_hash 97b9638bcde37ecfaec7d678aa21c495d0b89ec09ade5d1631c3b4fe458ccd5e

%global srcname pyswip

Name:           python-%{srcname}
Version:        0.3.3
Release:        4%{?dist}
Summary:        Python-SWI-Prolog bridge

License:        MIT
URL:            https://github.com/yuce/pyswip
Source0:        https://github.com/yuce/pyswip/archive/v%{version}/%{srcname}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

BuildRequires:  swi-prolog-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description
PySWIP is a Python - SWI-Prolog bridge enabling to query SWI-Prolog in your
Python programs. It features an (incomplete) SWI-Prolog foreign language
interface, a utility class that makes it easy querying with Prolog and also a
Pythonic interface.

%package     -n python3-%{srcname}
Summary:        %summary
Requires:       swi-prolog-core

%description -n python3-%{srcname}
PySWIP is a Python - SWI-Prolog bridge enabling to query SWI-Prolog in your
Python programs. It features an (incomplete) SWI-Prolog foreign language
interface, a utility class that makes it easy querying with Prolog and also a
Pythonic interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
