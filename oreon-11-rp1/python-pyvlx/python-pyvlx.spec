%global source0_hash c44fd2d9b2edb35acccb0efc067996b40abe52c1674b91482f24145cafe98ce4

%global pypi_name pyvlx

Name:           python-%{pypi_name}
Version:        0.2.26
Release:        5%{?dist}
Summary:        Python wrapper for the Velux KLF 200 API

License:        LGPL-3.0-or-later
URL:            https://github.com/Julius2342/pyvlx
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PyVLX allow you to control VELUX windows with Python. It uses the Velux
KLF 200 interface to control io-Homecontrol devices, e.g., Velux
Windows.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(typing-extensions)

%description -n python3-%{pypi_name}
PyVLX allow you to control VELUX windows with Python. It uses the Velux
KLF 200 interface to control io-Homecontrol devices, e.g., Velux
Windows.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

%check
%pytest -v test

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
