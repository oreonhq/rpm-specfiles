%global pypi_name pyqt_builder

Name:           PyQt-builder
Version:        1.19.1
Release:        3%{?dist}
Summary:        The PEP 517 compliant PyQt build system

License:        BSD-2-Clause
URL:            https://www.riverbankcomputing.com/software/pyqt/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt. It extends the sip build system and uses Qt's qmake to perform the
actual compilation and installation of extension modules.Projects that use
PyQt- builder provide an appropriate pyproject.toml file and an optional
project.py.

%prep
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
