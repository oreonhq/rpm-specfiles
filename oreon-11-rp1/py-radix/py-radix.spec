%global source0_hash 13eb2b0b228973c8fe79370db0d8c14ad74965ed8491d347483792cb20b8453b

Name: py-radix
Summary: Radix tree data structure for Python
Version: 0.10.0
Release: 19%{?dist}

URL: https://github.com/mjschultz/py-radix
Source0: https://github.com/mjschultz/py-radix/archive/v%{version}/%{name}-%{version}.tar.gz

# Define PY_SSIZE_T_CLEAN, use ssize_t as the index type (PEP 353)
# Fixes Python 3.10 failures, https://bugzilla.redhat.com/1899466
Patch1: https://github.com/mjschultz/py-radix/pull/55.patch#/py-radix-0.10.0-py_ssize_t_clean.patch
# Change away from deprecated assertEquals and assertNotEquals to assertEqual
# Fixes Python 3.12 failures, https://bugzilla.redhat.com/2175152
Patch2: https://github.com/mjschultz/py-radix/pull/44.patch#/py-radix-0.10.0-assertequal.patch
# Change incompatible pointer type from RadixNodeObject to PyObject
# Fixes Python 3.13 failures, https://bugzilla.redhat.com/2259528
Patch3: https://github.com/mjschultz/py-radix/pull/58.patch#/py-radix-0.10.0-pyobject-type.patch

License: BSD-4-Clause AND ISC
BuildRequires: gcc

%description
py-radix is an implementation of a radix tree for Python, which
supports storage and lookups of IPv4 and IPv6 networks.

The radix tree (a.k.a Patricia tree) is the data structure most
commonly used for routing table lookups. It efficiently stores
network prefixes of varying lengths and allows fast lookups of
containing networks. py-radix's implementation is built solely
for networks (the data structure itself is more general).

%package -n python3-%{name}
Summary: Radix tree data structure for Python

BuildRequires: python3-devel
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires: python3-setuptools
%endif
# Needed for tests
BuildRequires: python3-pytest

%if 0%{?rhel} && 0%{?rhel} < 9
%{?python_provide:%python_provide python3-%{name}}
%endif

%description -n python3-%{name}
py-radix is an implementation of a radix tree for Python, which
supports storage and lookups of IPv4 and IPv6 networks.

The radix tree (a.k.a Patricia tree) is the data structure most
commonly used for routing table lookups. It efficiently stores
network prefixes of varying lengths and allows fast lookups of
containing networks. py-radix's implementation is built solely
for networks (the data structure itself is more general).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -f inet_ntop.c strlcpy.c
touch inet_ntop.c strlcpy.c

%if 0%{?fedora} || 0%{?rhel} >= 9
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_wheel
%else
%py3_build
%endif

%install
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_install
%pyproject_save_files -l radix
%else
%py3_install
%endif

%check
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_check_import
%endif

%pytest -v

%if 0%{?fedora} || 0%{?rhel} >= 9
%files -n python3-%{name} -f %{pyproject_files}
%else
%files -n python3-%{name}
%license LICENSE
%{python3_sitearch}/py_radix*
%{python3_sitearch}/radix*
%endif
%doc README.rst

%changelog
%autochangelog
