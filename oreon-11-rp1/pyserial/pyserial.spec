%global source0_hash 3c77e014170dfffbd816e6ffc205e9842efb10be9f58ec16d3e8675b4925cddb
Summary:        Python serial port access library
Name: pyserial
Version: 3.5
Release:        16%{?dist}
Source0:        https://files.pythonhosted.org/packages/source/p/pyserial/pyserial-3.5.tar.gz
License: BSD-3-Clause
URL: http://pypi.python.org/pypi/pyserial
BuildArch: noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-pyserial
Summary:        Python serial port access library
Conflicts: python2-pyserial < 3.4-6
%description -n python3-pyserial

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
export UNZIP="-aa"
%setup -q

# Python 3.13+ has removed unittest.findTestCases()
# Reported upstream: https://github.com/pyserial/pyserial/issues/754
sed -i 's/unittest.findTestCases(module)/unittest.TestLoader().loadTestsFromModule(module)/' test/run_all_tests.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-pyserial usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONPATH=%{buildroot}/%{python3_sitelib} %{python3} test/run_all_tests.py
%files -f %{oreon_filedir}/main.list
%files -n python3-pyserial -f %{oreon_filedir}/python3-pyserial.list

%changelog

%autochangelog
