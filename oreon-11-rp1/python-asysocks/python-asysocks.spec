%global source0_hash 64cd44b4c07abb37ea0d910840c791a32b228ae28db68a5eee008dc1807535a2

%global pypi_name asysocks

Name:           python-%{pypi_name}
Version:        0.2.18
Release:        %autorelease
Summary:        Socks5/Socks4 client and server library

License:        MIT
URL:            https://github.com/skelsec/asysocks
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
A Python Socks5/Socks4 client and server library.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' asysocks/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/asysock*

%changelog
%autochangelog
