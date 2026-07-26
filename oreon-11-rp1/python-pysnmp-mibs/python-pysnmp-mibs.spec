%global source0_hash 00fa321ca598e8a14c0ad98702bf10fb5e9d57b7d06bb99dc818fea07683720c

# Created by pyp2rpm-3.3.8
%global pypi_name pysnmp-mibs
%global pypi_version 0.1.6

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        PySNMP MIBs
License:        BSD-2-Clause
URL:            https://github.com/etingof/pysnmp-mibs
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
A collection of IETF & IANA MIBs compiled into PySNMP classes.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides    python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pysnmp_mibs

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.txt

%changelog
%autochangelog
