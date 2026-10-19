%global source0_hash 51b3433123d85a36a7dde2c932b157783336eb4fbc256b27680122496b4a8ae8
%global owner michaeljones
%global srcname breathe
Name:           python-%{srcname}
Version:        5.0.0
Release:        1%{?dist}
Summary:        Adds support for Doxygen xml output to reStructuredText and Sphinx
License:        BSD-3-Clause
URL:            https://github.com/%{owner}/%{srcname}
Source0:        https://github.com/michaeljones/breathe/archive/refs/tags/v%{version}.tar.gz#/python-breathe-5.0.0.tar.gz
Patch0:         breathe-doxygen-1.16-tests.patch
BuildArch:      noarch
%global _docdir_fmt %{name}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.7
Requires:       python3-breathe = %{version}-%{release}
# /oreon:deps
%package -n       python3-breathe+build
Summary:        Metapackage for python3-breathe build extras
Requires:       python3-breathe = %{version}-%{release}
Requires:       python3dist(setuptools) >= 80.9.0
Provides:       python3dist(breathe[build]) = %{version}-%{release}

%description -n python3-breathe+build
Metapackage for python3-breathe build extras.

%package -n       python3-breathe+docs
Summary:        Metapackage for python3-breathe docs extras
Requires:       python3-breathe = %{version}-%{release}
Provides:       python3dist(breathe[docs]) = %{version}-%{release}

%description -n python3-breathe+docs
Metapackage for python3-breathe docs extras.

%package -n       python3-breathe+lint
Summary:        Metapackage for python3-breathe lint extras
Requires:       python3-breathe = %{version}-%{release}
Requires:       python3dist(ruff) == 0.9.2
Requires:       python3dist(mypy) >= 1
Requires:       python3dist(pytest) >= 8.0
Provides:       python3dist(breathe[lint]) = %{version}-%{release}

%description -n python3-breathe+lint
Metapackage for python3-breathe lint extras.

%package -n       python3-breathe+test
Summary:        Metapackage for python3-breathe test extras
Requires:       python3-breathe = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.0
Provides:       python3dist(breathe[test]) = %{version}-%{release}

%description -n python3-breathe+test
Metapackage for python3-breathe test extras.

%description

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        Adds support for Doxygen xml output to reStructuredText and Sphinx
Requires:       doxygen >= 1.8.4
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%description -n python%{python3_pkgversion}-%{srcname}

%package        doc
Summary:        Documentation files for %{srcname}
License:        BSD-3-Clause AND Zlib
%description    doc
This package contains documentation for developer documentation for %{srcname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version} -p1

%build

%make_build parser
%pyproject_wheel
%if %{with doc}
%make_build SPHINXOPTS="-v -E" DOXYGEN=$(which doxygen) PYTHONPATH=$(pwd) html
rm documentation/build/html/.buildinfo
%endif
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/breathe* usr/lib64/python3*/site-packages/breathe* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v tests
%files
%files -n python3-breathe -f %{oreon_filedir}/python3-breathe.list
%files -n python-breathe-doc -f %{oreon_filedir}/python-breathe-doc.list

%changelog

%autochangelog
