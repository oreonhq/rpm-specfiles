%global source0_hash 1672b4bb19a060a53dd0518cc8f70fc83591c7246e532223459f85d338c60f55

%global srcname modernize

Name:           python-modernize
Version:        0.8.0
Release:        21%{?dist}
Summary:        Modernizes Python code for eventual Python 3 migration

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/modernize
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This library is a very thin wrapper around lib2to3 to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It attempts, but does not guarantee, to generate a Python 2/3 compatible
codebase.  The code that it generates needs python2.6+ and has a runtime
dependency on python-six.

%package -n python3-modernize
Summary:        %{summary}
%{?python_provide:%python_provide python3-modernize}
Provides: python-modernize = %{version}-%{release}
Obsoletes: python-modernize < 0.4-3

%description -n python3-modernize
This library is a very thin wrapper around lib2to3 to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It attempts, but does not guarantee, to generate a Python 2/3 compatible
codebase.  The code that it generates needs python2.6+ and has a runtime
dependency on python-six.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-modernize
%doc README.rst
%{python3_sitelib}/modernize*
%{python3_sitelib}/libmodernize*
%{python3_sitelib}/__pycache__/modernize*
%{_bindir}/python-modernize
%{_bindir}/modernize

%changelog
%autochangelog
