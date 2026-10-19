%global source0_hash 143bc39bc2796920871d2b224bdede8cd720f2a8539784a4b256c1495128a72d
Name:           python-utils
Version:        4.0.1
Release:        1%{?dist}
Summary:        Python Utils is a module with some convenient utilities
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/WoLpH/python-utils
Source0:        https://github.com/WoLpH/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.13
BuildRequires:  python3dist(uv-build) >= 0.11
Requires:       python3-utils = %{version}-%{release}
# /oreon:deps
%package -n       python3-utils+loguru
Summary:        Metapackage for python3-utils loguru extras
Requires:       python3-utils = %{version}-%{release}
Provides:       python3dist(utils[loguru]) = %{version}-%{release}

%description -n python3-utils+loguru
Metapackage for python3-utils loguru extras.

%package -n       python3-utils+docs
Summary:        Metapackage for python3-utils docs extras
Requires:       python3-utils = %{version}-%{release}
Provides:       python3dist(utils[docs]) = %{version}-%{release}

%description -n python3-utils+docs
Metapackage for python3-utils docs extras.

%package -n       python3-utils+tests
Summary:        Metapackage for python3-utils tests extras
Requires:       python3-utils = %{version}-%{release}
Provides:       python3dist(utils[tests]) = %{version}-%{release}

%description -n python3-utils+tests
Metapackage for python3-utils tests extras.

%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. This module makes it easy to
execute common tasks in Python scripts such as converting text to numbers
and making sure a string is in unicode or bytes format.

%package -n     python3-utils
Summary:        Python Utils is a module with some convenient utilities
# oreon:reqs
Requires:       python3dist(typing-extensions) > 3.10.0.2
# /oreon:reqs
%description -n python3-utils
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. This module makes it easy to
execute common tasks in Python scripts such as converting text to numbers
and making sure a string is in unicode or bytes format.

%package        docs
Summary:        Documentation for python-utils
%description docs
Documentation for python-utils.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# Stop linting code in %%check and measuring coverage, this is upstream's business
sed -Ei "/'--cov/d" pyproject.toml

%build

%pyproject_wheel
sphinx-build docs html
rm -rf html/{.doctrees,.buildinfo,*.inv}
%install
%pyproject_install
%oreon_autofiles python3-utils usr/lib/python3*/site-packages/utils* usr/lib64/python3*/site-packages/utils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/utils* usr/lib64/python3*/site-packages/utils* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest --ignore _python_utils_tests/test_logger.py --ignore python_utils/loguru.py
%files
%files -n python3-utils -f %{oreon_filedir}/python3-utils.list
%files -n python-utils-docs -f %{oreon_filedir}/python-utils-docs.list

%changelog

%autochangelog
