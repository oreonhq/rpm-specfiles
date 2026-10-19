%global source0_hash cde91df156f8725a3d29a3cd153767a64f71c3903af98d29ae2a06f3cebb2b99
Name:           python-firehose
Version:        0.5
Release:        37%{?dist}
Summary:        Library for working with output from static code analyzers
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/fedora-static-analysis/firehose
Source0:        https://github.com/fedora-static-analysis/firehose/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-Remove-calls-to-deprecated-plistlib-function.patch
Patch1:         python-firehose-rm-python-mock-usage.patch
# oreon:deps
BuildRequires:  libxml2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
# /oreon:deps
%description

%package -n python3-firehose
Summary:        Library for working with output from static code analyzers
Requires:  python3-six
%{?python_provide:%python_provide python3-firehose}
%description -n python3-firehose

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n firehose-%{version}

# Change shebang according to Python version
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' firehose/parsers/cppcheck.py
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' firehose/parsers/gcc.py

sed -i 's/distutils\.core/setuptools/' setup.py

%build

%py3_build
%install
%py3_install
chmod +x %{buildroot}/%{python3_sitelib}/firehose/parsers/cppcheck.py
chmod +x %{buildroot}/%{python3_sitelib}/firehose/parsers/gcc.py
%oreon_autofiles python3-firehose usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} -m unittest discover -v
%files -f %{oreon_filedir}/main.list
%files -n python3-firehose -f %{oreon_filedir}/python3-firehose.list

%changelog

%autochangelog
