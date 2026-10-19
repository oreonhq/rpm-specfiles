%global source0_hash 339369a461bf3ded42d6fd2144ffcd242e85a9e7763496336e649eba1b528f7e
%bcond bootstrap 0
%bcond docs 1
%bcond tests %{without bootstrap}
Name:       python-SecretStorage
Version:    3.5.0
Release:        1%{?dist}
Summary:        Python bindings to FreeDesktop.org Secret Service API
URL:        https://github.com/mitya57/secretstorage
Source0:        https://github.com/mitya57/secretstorage/archive/%{version}/secretstorage-%{version}.tar.gz
License:    BSD-3-Clause
BuildArch:  noarch
%if %{with tests}
%endif
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-SecretStorage = %{version}-%{release}
# /oreon:deps
%description
This module provides a way for securely storing passwords and other secrets.

It uses D-Bus Secret Service API that is supported by GNOME Keyring (>= 2.30)
and KSecretsService.

The main classes provided are secretstorage.Item, representing a secret item
(that has a label, a secret and some attributes) and secretstorage.Collection,
a place items are stored in.

SecretStorage supports most of the functions provided by Secret Service,
including creating and deleting items and collections, editing items, locking
and unlocking collections (asynchronous unlocking is also supported).

%package -n python3-secretstorage
Summary:        Python bindings to FreeDesktop.org Secret Service API
%py_provides    python3-SecretStorage
%description -n python3-secretstorage
This module provides a way for securely storing passwords and other secrets.

It uses D-Bus Secret Service API that is supported by GNOME Keyring (>= 2.30)
and KSecretsService.

The main classes provided are secretstorage.Item, representing a secret item
(that has a label, a secret and some attributes) and secretstorage.Collection,
a place items are stored in.

SecretStorage supports most of the functions provided by Secret Service,
including creating and deleting items and collections, editing items, locking
and unlocking collections (asynchronous unlocking is also supported).

%package -n python3-secretstorage-doc
Summary:        SecretStorage documentation
%description -n python3-secretstorage-doc
Documentation for SecretStorage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir secretstorage-%{version}
%oreon_prep
%build

%pyproject_wheel
%if %{with docs}
sphinx-build-3 docs html
find build -name '.buildinfo' -delete -print
find build -name 'doctrees' -type d -print -exec rm -r '{}' +
%endif
%install
%pyproject_install
%oreon_autofiles python3-secretstorage usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-secretstorage-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%if %{with tests}
export %{py3_test_envvars}
for MOCK in /usr/share/libsecret/mock-service-{normal,only-plain,lock}.py; do
  xwfb-run -- dbus-launch --exit-with-session %{python3} tests/run_tests.py ${MOCK}
done
%endif
%files
%files -n python3-secretstorage -f %{oreon_filedir}/python3-secretstorage.list
%files -n python3-secretstorage-doc -f %{oreon_filedir}/python3-secretstorage-doc.list

%changelog

%autochangelog
