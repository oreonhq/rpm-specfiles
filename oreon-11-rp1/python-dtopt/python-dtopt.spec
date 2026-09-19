%global source0_hash 06ae07a12294a7ba708abaa63f838017d1a2faf6147a1e7a14ca4fa28f86da7f

Name:           python-dtopt
Summary:        Add options to doctest examples while they are running
Version:        0.1
Release:        56%{?dist}
License:        MIT

URL:            http://pypi.python.org/pypi/dtopt/
Source0:        http://pypi.python.org/packages/source/d/dtopt/dtopt-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
dtopts adds options to doctest examples while they are running. When\
using the doctest module it is often convenient to use the ELLIPSIS\
option, which allows you to use ... as a wildcard. But you either have\
to setup the test runner to use this option, or you must put #doctest:\
+ELLIPSIS on every example that uses this feature. dtopt lets you enable\
this option globally from within a doctest, by doing:\
>>> from dtopt import ELLIPSIS

%description %_description

%package -n python3-dtopt
Summary:        Add options to doctest examples while they are running
Version:        0.1

%description -n python3-dtopt
dtopts adds options to doctest examples while they are running. When
using the doctest module it is often convenient to use the ELLIPSIS
option, which allows you to use ... as a wildcard. But you either have
to setup the test runner to use this option, or you must put #doctest:
+ELLIPSIS on every example that uses this feature. dtopt lets you enable
this option globally from within a doctest, by doing:
>>> from dtopt import ELLIPSIS

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n dtopt-%{version}

# Remove bundled egg info if it exists.
rm -rf *.egg-info

# There is a print statement in the test that is not python3 compatible.
rm dtopt/tests.py*

%build
%py3_build

%install
%py3_install

%files -n python3-dtopt
%doc docs/*
%{python3_sitelib}/dtopt/
%{python3_sitelib}/dtopt*.egg-info/

%changelog
%autochangelog
