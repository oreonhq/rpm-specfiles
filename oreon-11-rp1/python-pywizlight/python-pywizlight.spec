%global source0_hash ec32e8df0285f1951a331f463c45f790e137294ea5d3a583502718b9a7db4a69

%global pypi_name pywizlight

Name:           python-%{pypi_name}
Version:        0.6.3
Release:        5%{?dist}
Summary:        Python connector for WiZ light devices

License:        MIT
URL:            https://github.com/sbidy/pywizlight
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python connector for WiZ light devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{pypi_name}
A Python connector for WiZ light devices.

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

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/wizlight

%changelog
%autochangelog
