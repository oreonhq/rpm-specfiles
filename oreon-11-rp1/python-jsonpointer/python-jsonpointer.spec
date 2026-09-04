%global source0_hash 585cee82b70211fa9e6043b7bb89db6e1aa49524340dde8ad6b63206ea689d88

%global pypi_name jsonpointer

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        Resolve JSON Pointers in Python

License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-pointer
Source0:        https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-2.4.tar.gz

BuildArch:      noarch

%global _description %{expand:
Library to resolve JSON Pointers according to RFC 6901.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%python3 -m unittest discover

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md AUTHORS
%{_bindir}/jsonpointer

%changelog
* Fri Sep 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.1-1
- Update to 3.1.1

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4-9
- Prepare for Oreon 11 (RP1)
