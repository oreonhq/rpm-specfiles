%global source0_hash e999a1c5197d6e0a2abfe0cb5dee509725e29aa720c9bad169cd75961741c9b3

%global srcname represent
%global sum Create __repr__ automatically or declaratively

Name:           python-%{srcname}
Version:        2.2.0
Release:        1%{?dist}
Summary:        %{sum}
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/RazerM/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description
Python package which creates __repr__ automatically or declaratively.

%package -n python3-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python3 package which creates __repr__ automatically or declaratively.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
