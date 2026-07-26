%global source0_hash aeebb2a2b5014a78307d663807337c0de8be1ff27474ea6808928ca948e88381

%global module uhashring

Name:           python-%{module}
Version:        2.3
Release:        14%{?dist}
Summary:        Python module uhashring

License:        BSD-3-Clause
URL:            https://github.com/ultrabug/uhashring/
Source:         https://github.com/ultrabug/%{module}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Required to run unit tests
BuildRequires:  python3-pytest
BuildRequires:  python3-memcached

%global _description %{expand:
uhashring implements consistent hashing in pure Python.}

%description %_description

%package -n python3-%{module}
Summary:        %{summary}

%description -n python3-%{module}
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{module}-%{version}

sed -i 's/ *"black",//g' pyproject.toml
sed -i 's/ *"flake8",//g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{module}

%check
%pytest

%files -n python3-%{module} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
