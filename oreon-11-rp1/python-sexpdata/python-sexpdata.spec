%global source0_hash a36c99143e778718b33d06db46d8f842736296f44358504c48fc8732663943a8

%global srcname sexpdata

%global _description %{expand:sexpdata is a simple S-expression parser/serializer. It has simple load and dump
functions like pickle, json or PyYAML module.}

Name:           python-%{srcname}
Version:        1.0.2
Release:        9%{?dist}
Summary:        S-expression parser for Python

License:        BSD-2-Clause
URL:            https://sexpdata.readthedocs.io/
Source0:        https://github.com/jd-boyd/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
