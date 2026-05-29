%global source0_hash 0e56ee44222d2df37c337c376973861af300a7f86b8ff9dc199c2b3349a3d204

# NOTE: tests are disabled since should_be has not yet been packaged.

Name:           python-gssapi
Version:        1.7.3
Release:        16%{?dist}
Summary:        Python Bindings for GSSAPI (RFC 2743/2744 and extensions)

License:        ISC
URL:            https://github.com/pythongssapi/python-gssapi
Source0:        https://github.com/pythongssapi/python-gssapi/releases/download/v1.7.3/python-gssapi-1.7.3.tar.gz
# https://github.com/pythongssapi/python-gssapi/pull/321
Patch0:         cython3.patch

BuildRequires:  krb5-devel >= 1.19
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-Cython

# For autosetup
BuildRequires: git-core

%global _description\
A set of Python bindings to the GSSAPI C library providing both\
a high-level pythonic interfaces and a low-level interfaces\
which more closely matches RFC 2743.  Includes support for\
RFC 2743, as well as multiple extensions.

%description %_description

%package -n python3-gssapi
Summary:        Python 3 Bindings for GSSAPI (RFC 2743/2744 and extensions)
Requires:       krb5-libs >= 1.19

%description -n python3-gssapi %_description

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files gssapi

%check
# Check import everything except the tests, as we don't have the tests deps
%pyproject_check_import -e 'gssapi.tests*'

%files -n python3-gssapi -f %{pyproject_files}
%doc README.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.3-16
- Import
