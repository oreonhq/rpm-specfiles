%global source0_hash c9f829c363e12b886633dc4e3ecc03e5c06b14086972819bd8dc1e497f2e7d8b
Name:           python3-mypy
Version:        2.3.1
Release:        1%{?dist}
Summary:        A static type checker for Python
License:        MIT and Apache-2.0
URL:            https://github.com/python/mypy
Source0:        https://github.com/python/mypy/archive/v%{version}/mypy-%{version}.tar.gz
Requires:  python3-typing-extensions
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(ast-serialize) < 1.0.0
BuildRequires:  python3dist(ast-serialize) >= 0.6.0
BuildRequires:  python3dist(librt) >= 0.13.0
BuildRequires:  python3dist(mypy-extensions) >= 1.0.0
BuildRequires:  python3dist(pathspec) >= 1.0.0
BuildRequires:  python3dist(setuptools) >= 77.0.3
BuildRequires:  python3dist(tomli) >= 1.1.0
BuildRequires:  python3dist(typing-extensions) >= 4.14.0
BuildRequires:  python3dist(typing-extensions) >= 4.6.0
Requires:       python3-python3-mypy = %{version}-%{release}
# /oreon:deps
%package -n       python3-python3-mypy+dmypy
Summary:        Metapackage for python3-python3-mypy dmypy extras
Requires:       python3-python3-mypy = %{version}-%{release}
Requires:       python3dist(psutil) >= 4.0
Provides:       python3dist(python3-mypy[dmypy]) = %{version}-%{release}

%description -n python3-python3-mypy+dmypy
Metapackage for python3-python3-mypy dmypy extras.

%package -n       python3-python3-mypy+mypyc
Summary:        Metapackage for python3-python3-mypy mypyc extras
Requires:       python3-python3-mypy = %{version}-%{release}
Requires:       python3dist(setuptools) >= 50
Provides:       python3dist(python3-mypy[mypyc]) = %{version}-%{release}

%description -n python3-python3-mypy+mypyc
Metapackage for python3-python3-mypy mypyc extras.

%package -n       python3-python3-mypy+reports
Summary:        Metapackage for python3-python3-mypy reports extras
Requires:       python3-python3-mypy = %{version}-%{release}
Provides:       python3dist(python3-mypy[reports]) = %{version}-%{release}

%description -n python3-python3-mypy+reports
Metapackage for python3-python3-mypy reports extras.

%package -n       python3-python3-mypy+install-types
Summary:        Metapackage for python3-python3-mypy install-types extras
Requires:       python3-python3-mypy = %{version}-%{release}
Provides:       python3dist(python3-mypy[install-types]) = %{version}-%{release}

%description -n python3-python3-mypy+install-types
Metapackage for python3-python3-mypy install-types extras.

%package -n       python3-python3-mypy+faster-cache
Summary:        Metapackage for python3-python3-mypy faster-cache extras
Requires:       python3-python3-mypy = %{version}-%{release}
Provides:       python3dist(python3-mypy[faster-cache]) = %{version}-%{release}

%description -n python3-python3-mypy+faster-cache
Metapackage for python3-python3-mypy faster-cache extras.

%package -n       python3-python3-mypy+native-parser
Summary:        Metapackage for python3-python3-mypy native-parser extras
Requires:       python3-python3-mypy = %{version}-%{release}
Provides:       python3dist(python3-mypy[native-parser]) = %{version}-%{release}

%description -n python3-python3-mypy+native-parser
Metapackage for python3-python3-mypy native-parser extras.

%description
Mypy is an optional static type checker for Python.  You can add type
hints to your Python programs using the upcoming standard for type
annotations introduced in Python 3.5 beta 1 (PEP 484), and use mypy to
type check them statically. Find bugs in your programs without even
running them!

%python_extras_subpkg -n %{name} -i %{python3_sitelib}/mypy-*.dist-info dmypy,mypyc,reports,install-types,faster-cache

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mypy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'mypy %{version}-dev' \
        --no-discard-stderr -o %{buildroot}%{_mandir}/man1/mypy.1 \
        %{buildroot}%{_bindir}/mypy
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'mypy stubgen %{version}-dev' \
        --no-discard-stderr -o %{buildroot}%{_mandir}/man1/stubgen.1 \
        %{buildroot}%{_bindir}/stubgen
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog
