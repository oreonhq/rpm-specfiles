%global source0_hash 3757b049728580d516c0af50e11eed050c8e2c1815b221954c635bde455dcc78

Name:           python-fastjsonschema
Version:        2.21.2
Release:        4%{?dist}
Summary:        Fastest Python implementation of JSON schema

License:        BSD-3-Clause
URL:            https://github.com/horejsek/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
fastjsonschema implements validation of JSON documents by JSON schema.
The library implements JSON schema drafts 04, 06 and 07.
The main purpose is to have a really fast implementation.}

%description %_description

%package -n     python3-fastjsonschema
Summary:        %{summary}

%description -n python3-fastjsonschema %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fastjsonschema

%check
%pytest -m "not benchmark"

%files -n python3-fastjsonschema -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
