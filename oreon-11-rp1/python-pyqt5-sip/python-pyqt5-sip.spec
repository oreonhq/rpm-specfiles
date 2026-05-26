# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 0eab72bcb628f1926bf5b9ac51259d4fa18e8b2a81d199071135458f7d087ea8
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt5_sip/pyqt5_sip-12.17.1.tar.gz

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
%oreon_verify_sources
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
