%global source0_hash 6af6646ba29668751b039bfdced51642cb510e300796b58a4d68b7f956a024d8

%global pypi_name pyqt_builder

Name:           PyQt-builder
Version:        1.19.1
Release:        3%{?dist}
Summary:        The PEP 517 compliant PyQt build system

License:        BSD-2-Clause
URL:            https://www.riverbankcomputing.com/software/pyqt/
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt_builder/pyqt_builder-1.19.1.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt. It extends the sip build system and uses Qt's qmake to perform the
actual compilation and installation of extension modules.Projects that use
PyQt- builder provide an appropriate pyproject.toml file and an optional
project.py.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyqtbuild
# These dll files are from openssl and microsoft visiual studio
# While we can redistribute them, we don't have source and it's 
# unlikely anyone will want to bundle a windows executable from linux.
rm -rf %{buildroot}/%{python3_sitelib}/pyqtbuild/bundle/dlls
sed -r -i '/\/pyqtbuild\/bundle\/dlls/d' %{pyproject_files}

%check
%py3_check_import pyqtbuild

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/pyqt-bundle
%{_bindir}/pyqt-qt-wheel

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.19.1-3
- Prepare for Oreon 11 (RP1)
