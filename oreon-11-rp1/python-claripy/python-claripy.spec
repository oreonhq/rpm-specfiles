%global source0_hash 0bcff6ad72b91b96cd53903cfbe08ab501529c933338d38d40f3a87623e3854b

%global pypi_name claripy

Name:           python-%{pypi_name}
Version:        9.2.189
Release:        2%{?dist}
Summary:        Abstraction layer for constraint solvers

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/angr/claripy
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Claripy is an abstracted constraint-solving wrapper.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3-z3

%description -n python3-%{pypi_name}
Claripy is an abstracted constraint-solving wrapper.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
# Remove installation requirement. Fedora is using a different name, see above
sed -i 's/, "z3-solver==4.13.0.0"//' pyproject.toml

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

%changelog
%autochangelog
