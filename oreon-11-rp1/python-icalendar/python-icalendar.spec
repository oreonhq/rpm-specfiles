%global source0_hash dc211532733d1d2f6b713fdcd66f5397dea64abca10d9bdca99220e57fd4fab2

Name:           python-icalendar
Version:        7.3.0
Release:        1%{?dist}
Summary:        Parser/generator of iCalendar files following the RFC 2445

License:        BSD-2-Clause
URL:            http://pypi.python.org/pypi/icalendar
Source0:        https://github.com/collective/icalendar/archive/v%{version}/%{version}.tar.gz

Patch0:         hatch.patch
Patch1:         tzdata.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest

%global _description\
iCalendar specification (RFC 2445) defines calendaring format used\
by many applications (Zimbra, Thunderbird and others). This\
module is a parser/generator of iCalendar files for use with\
Python. It follows the RFC 2445 (iCalendar) specification.\
The aim is to make a package that is fully compliant with RFC 2445,\
well designed, simple to use and well documented.\

%description %_description

%package -n python3-icalendar
Summary:        Parser/generator of iCalendar files following the RFC 2445 for Python 3
Requires:       python3-pytz
Requires:       python3-dateutil

%description -n python3-icalendar
iCalendar specification (RFC 2445) defines calendaring format used\
by many applications (Zimbra, Thunderbird and others). This\
module is a parser/generator of iCalendar files for use with\
Python. It follows the RFC 2445 (iCalendar) specification.\
The aim is to make a package that is fully compliant with RFC 2445,\
well designed, simple to use and well documented.\

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n icalendar-%{version}%{?veradd}

%patch -P 0 -p0
%patch -P 1 -p0

# we have only 2.7 and 3.3
sed -i 's/py26,//' tox.ini

rm -rf %{py3dir}
cp -a . %{py3dir}

%generate_buildrequires
%pyproject_buildrequires

%build
pushd %{py3dir}
%pyproject_wheel
popd

%install
pushd %{py3dir}
%pyproject_install
popd

%check
pushd %{py3dir}
%{__python3} -m pytest src/icalendar/tests
popd

%files -n python3-icalendar
%doc README.rst CHANGES.rst LICENSE.rst
%{python3_sitelib}/icalendar
%{python3_sitelib}/*.dist-info
%{_bindir}/icalendar

%changelog
%autochangelog
