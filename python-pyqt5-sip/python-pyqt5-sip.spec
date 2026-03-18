%global pypi_name pyqt5_sip
%global _sip_api_major 12
%global _sip_api_minor 17
%global _sip_api %{_sip_api_major}.%{_sip_api_minor}

Name:           python-pyqt5-sip
Version:        12.17.1
Release:        2%{?dist}
Summary:        The sip module support for PyQt5

License:        BSD-2-Clause
URL:            https://www.riverbankcomputing.com/software/sip/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
The sip extension module provides support for the PyQt5 package.
}

%description %_description

%package -n     python3-pyqt5-sip
Summary:        %{summary}
Provides: python3-pyqt5-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python3-pyqt5-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}

%description -n python3-pyqt5-sip %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files PyQt5

%check
%py3_check_import PyQt5.sip

%files -n python3-pyqt5-sip -f %{pyproject_files}
%doc README

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.17.1-2
- Prepare for Oreon 11 (RP1)
