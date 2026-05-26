Name: pyusb
Version: 1.3.1
Release: 7%{?dist}
Summary: Python bindings for libusb
License: BSD-3-Clause
URL: https://github.com/pyusb/pyusb/
Source0:        https://files.pythonhosted.org/packages/source/p/pyusb/pyusb-1.3.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 3af070b607467c1c164f49d5b0caabe8ac78dbed9298d703a8dbf9df4052d17e
%global source0_file pyusb-1.3.1.tar.gz
# oreon url source checksums end
BuildRequires: libusb1
BuildArch: noarch

%global _description\
PyUSB provides easy USB access to python. The module contains classes and\
methods to support most USB operations.

%description %_description

%package -n python3-pyusb
Summary:       %summary
BuildRequires: python3-devel
BuildRequires:  python3-setuptools_scm
Requires:       libusb1

%description -n python3-pyusb
PyUSB provides easy USB access to python. The module contains classes and 
methods to support most USB operations.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pyusb-1.3.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3af070b607467c1c164f49d5b0caabe8ac78dbed9298d703a8dbf9df4052d17e" || { echo "oreon: Source0 SHA256 mismatch for pyusb-1.3.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup
sed -i -e 's/\r//g' README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'

%check
%pyproject_check_import

cd tests
%{py3_test_envvars} %{python3} ./testall.py

%files -n python3-pyusb -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-7
- Prepare for Oreon 11 (RP1)
