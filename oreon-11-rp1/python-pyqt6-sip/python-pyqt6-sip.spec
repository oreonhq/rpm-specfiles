%global source0_hash d463af37738bda1856c9ef513e5620a37b7a005e9d589c986c3304db4a8a14d3

%global pkg_name pyqt6-sip
%global pypi_name pyqt6_sip
%global _sip_api_major 13
%global _sip_api_minor 10
%global _sip_api %{_sip_api_major}.%{_sip_api_minor}

Name:           python-%{pkg_name}
Version:        13.11.0
Release:        2%{?dist}
Summary:        The sip module support for PyQt6

License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.riverbankcomputing.com/software/sip/
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt6_sip/pyqt6_sip-13.11.0.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
The sip extension module provides support for the PyQt6 package.
}

%description %_description

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}
Provides: python3-pyqt6-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python3-pyqt6-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}

%description -n python3-%{pkg_name} %_description
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l PyQt6


%check
%pyproject_check_import


%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.11.0-2
- Prepare for Oreon 11 (RP1)
