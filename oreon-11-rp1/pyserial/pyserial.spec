Summary: Python serial port access library
Name: pyserial
Version: 3.5
Release: 16%{?dist}
Source0:        https://files.pythonhosted.org/packages/source/p/pyserial/pyserial-3.5.tar.gz
# oreon url source checksums begin
%global source0_sha256 3c77e014170dfffbd816e6ffc205e9842efb10be9f58ec16d3e8675b4925cddb
%global source0_file pyserial-3.5.tar.gz
# oreon url source checksums end
License: BSD-3-Clause
URL: http://pypi.python.org/pypi/pyserial
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildArch: noarch

%global _description\
This module encapsulates the access for the serial port. It provides backends\
for standard Python running on Windows, Linux, BSD (possibly any POSIX\
compliant system) and Jython. The module named "serial" automatically selects\
the appropriate backend.

%description %_description


%package -n python3-pyserial
Summary: %{summary}
Conflicts: python2-pyserial < 3.4-6

%description -n python3-pyserial %_description


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pyserial-3.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3c77e014170dfffbd816e6ffc205e9842efb10be9f58ec16d3e8675b4925cddb" || { echo "oreon: Source0 SHA256 mismatch for pyserial-3.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
export UNZIP="-aa"
%setup -q

# Python 3.13+ has removed unittest.findTestCases()
# Reported upstream: https://github.com/pyserial/pyserial/issues/754
sed -i 's/unittest.findTestCases(module)/unittest.TestLoader().loadTestsFromModule(module)/' test/run_all_tests.py

%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{python3} test/run_all_tests.py


%files -n python3-pyserial
%doc LICENSE.txt CHANGES.rst README.rst examples
%{python3_sitelib}/serial
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{_bindir}/pyserial-miniterm
%{_bindir}/pyserial-ports

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.5-16
- Prepare for Oreon 11 (RP1)
