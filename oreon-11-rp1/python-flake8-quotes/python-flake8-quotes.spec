%global source0_hash 3d372716b21b3885a387e7f4fd0669833e0863cf69dd1262db06a58da1ae1417

%global srcname flake8-quotes

Name:           python-%{srcname}
Version:        3.4.0
Release:        8%{?dist}
Summary:        Flake8 extension for checking quotes in python

License:        MIT
URL:            https://github.com/zheller/flake8-quotes
Source0:        https://github.com/zheller/flake8-quotes/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
This package adds flake8 warnings with the prefix Q0:

- Q000: Remove bad quotes
- Q001: Remove bad quotes from multiline string
- Q002: Remove bad quotes from docstring
- Q003: Change outer quotes to avoid escaping inner quotes}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l flake8_quotes

%check
%pytest test

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
