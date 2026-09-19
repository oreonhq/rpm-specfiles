%global source0_hash e881fdc7da53a6bc9d429c84ed5c8424d38ecc5da2232e1ed5bbd37b324b88c0

%global pypi_name tubes

# Something broken in Twisted breaks these tests
%bcond check 1

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        8%{?dist}
Summary:        Flow control and backpressure for event-driven applications

License:        MIT
URL:            https://github.com/twisted/tubes/
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(twisted)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(setuptools)

%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unused dependency
sed -e '/"characteristic",/d' -i setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with check}
%check
%tox
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
