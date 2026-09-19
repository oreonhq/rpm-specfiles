%global source0_hash c43c9e0b4ad4e21ec8efae9f10e640c3785ac1a69ed32db9ba7f92cf52a91159

%global pypi_name cooldict

Name:           python-%{pypi_name}
Version:        1.04
Release:        26%{?dist}
Summary:        Some useful dict-like structures

License:        BSD-2-Clause
URL:            https://github.com/zardus/cooldict
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Helper for handling dictonery-like structures.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
sed -i 's|collections.MutableMapping|collections.abc.MutableMapping|g' cooldict.py
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
