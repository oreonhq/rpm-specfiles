%global source0_hash 4ffd0d13f9bb60f19f909560805da189e57c619a8d9c1bb61a7400a442dcfce9

Name: python-bitmath
Version: 1.3.3.1
Release: 8%{?dist}
Summary: Aids representing and manipulating file sizes in various prefix notations

License: MIT
URL: https://github.com/tbielawa/bitmath

Source: https://github.com/tbielawa/bitmath/archive/%{version}.tar.gz
# Maintainers, please upstream
Patch:  python-bitmath-rm-python-mock-usage.diff

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%global _description %{expand:
bitmath simplifies many facets of interacting with file sizes in
various units. Examples include: converting between SI and NIST prefix
units (GiB to kB), converting between units of the same type (SI to
SI, or NIST to NIST), basic arithmetic operations (subtracting 42KiB
from 50GiB), and rich comparison operations (1024 Bytes == 1KiB),
bitwise operations, sorting, automatic best human-readable prefix
selection, and completely customizable formatting.

In addition to the conversion and math operations, bitmath provides
human readable representations of values which are suitable for use in
interactive shells as well as larger scripts and applications. It can
also read the capacity of system storage devices. bitmath can parse
strings (like "1 KiB") into proper objects and has support for
integration with the argparse module as a custom argument type and the
progressbar module as a custom file transfer speed widget.

bitmath is thoroughly unittested, with almost 200 individual tests (a
number which is always increasing). bitmath's test-coverage is almost
always at 100%.}

%description %{_description}

######################################################################
# Sub-package setup
%package -n python3-bitmath
Summary: Aids representing and manipulating file sizes in various prefix notations
%{?python_provide:%python_provide python3-bitmath}

%description -n python3-bitmath %{_description}

######################################################################
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n bitmath-%{version}
%generate_buildrequires
%pyproject_buildrequires

######################################################################
%build
%pyproject_wheel

######################################################################
%install
%pyproject_install
%pyproject_save_files bitmath

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
cp -v *.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}/docs
cp -v -r docsite/source/* $RPM_BUILD_ROOT/%{_docdir}/%{name}/docs/
rm -f $RPM_BUILD_ROOT/%{_docdir}/%{name}/docs/NEWS.rst

######################################################################
%check
# We can't run the progressbar and argparse tests in python3 until
# progressbar has a python3 package available :(
#
# Skip those tests for now and run the rest
%pytest -v --ignore=tests/test_argparse_type.py \
           --ignore=tests/test_progressbar.py

######################################################################
%files -n python3-bitmath -f %{pyproject_files}
%doc README.rst NEWS.rst
%doc %{_mandir}/man1/bitmath.1*
%doc %{_docdir}/%{name}/docs/
%{_bindir}/bitmath

######################################################################
%changelog
%autochangelog
