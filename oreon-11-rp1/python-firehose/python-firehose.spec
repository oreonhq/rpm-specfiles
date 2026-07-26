%global source0_hash cde91df156f8725a3d29a3cd153767a64f71c3903af98d29ae2a06f3cebb2b99

Name:           python-firehose
Version:        0.5
Release:        37%{?dist}
Summary:        Library for working with output from static code analyzers

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/fedora-static-analysis/firehose
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# https://github.com/fedora-static-analysis/firehose/pull/42
Patch0:         0001-Remove-calls-to-deprecated-plistlib-function.patch

# Maintainers, please upstream
Patch1:         python-firehose-rm-python-mock-usage.patch

BuildRequires:  libxml2
# ^^^: for xmllint
# ^^^: used during selftests

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

%global _description\
"firehose" is a Python package intended for managing the results from\
code analysis tools (e.g. compiler warnings, static analysis, linters,\
etc).\
\
It currently provides parsers for the output of gcc, clang-analyzer and\
cppcheck.  These parsers convert the results into a common data model of\
Python objects, with methods for lossless roundtrips through a provided\
XML format.  There is also a JSON equivalent.\

%description %_description

%package -n python3-firehose
Summary:        Library for working with output from static code analyzers
Requires:  python3-six
%{?python_provide:%python_provide python3-firehose}

%description -n python3-firehose %_description

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

%check
%{__python3} -m unittest discover -v

%files -n python3-firehose
%doc README.rst lgpl-2.1.txt examples firehose.rng
%{python3_sitelib}/firehose/
%{python3_sitelib}/firehose-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
