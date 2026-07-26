%global source0_hash 607ce138fc714cf5bdc4c04fcf3b181d40a6f0b8387e243d55ebbb527c964853

%global pypi_name archinfo

Name:           python-%{pypi_name}
Version:        9.2.189
Release:        2%{?dist}
Summary:        Collection of classes that contain architecture-specific information

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/angr/archinfo
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
