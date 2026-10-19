%global source1_hash 6093195d65f7e3566f38e3d9f9e0b6c3615e92774de904028937b18d941f699b
%global source0_hash 6549c0b3e41d1ebe0c94a1be63c25eec918191462b602ab6f47d4a5fa709c3e4
%global source2_key_fpr 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D
Name:           pam_wrapper
Version:        1.1.8
Release:        1%{?dist}
Summary:        A tool to test PAM applications and PAM modules
License:        GPL-3.0-or-later
Url:            http://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        pam_wrapper.keyring
Recommends:     cmake
Recommends:     pkgconfig
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gpgverify
BuildRequires:  libcmocka-devel
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
This component of cwrap allows you to either test your PAM (Linux-PAM
and OpenPAM) application or module.

For testing PAM applications, simple PAM module called pam_matrix is
included. If you plan to test a PAM module you can use the pamtest library,
which simplifies testing of modules. You can combine it with the cmocka
unit testing framework or you can use the provided Python bindings to
write tests for your module in Python.

%package -n libpamtest
Summary:        A tool to test PAM applications and PAM modules
License:        GPL-3.0-or-later
Requires:       pam_wrapper = %{version}-%{release}
%description -n libpamtest
If you plan to test a PAM module you can use this library, which simplifies
testing of modules.

%package -n libpamtest-devel
Summary:        A tool to test PAM applications and PAM modules
License:        GPL-3.0-or-later
Requires:       pam_wrapper = %{version}-%{release}
Requires:       libpamtest = %{version}-%{release}
Recommends:     cmake
Recommends:     pkgconfig
%description -n libpamtest-devel
If you plan to develop tests for a PAM module you can use this library,
which simplifies testing of modules. This sub package includes the header
files for libpamtest.

%package -n libpamtest-doc
Summary:        The libpamtest API documentation
License:        GPL-3.0-or-later
%description -n libpamtest-doc
Documentation for libpamtest development.

%package -n python3-libpamtest
Summary:        A python wrapper for libpamtest
License:        GPL-3.0-or-later
Requires:       pam_wrapper = %{version}-%{release}
Requires:       libpamtest = %{version}-%{release}
%description -n python3-libpamtest
If you plan to develop python tests for a PAM module you can use this
Python module to quickly write tests in Python.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Not compatible with Python 3.12 headers
sed -i -e '/Werror=declaration-after-statement/d' CompilerChecks.cmake
# renamed in Python 3.2, old name dropped in 3.12
sed -i -e 's/assertRaisesRegexp/assertRaisesRegex/' tests/pypamtest_test.py

%build

%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DUNIT_TESTING=ON \
  -DPYTHON_INSTALL_SITEARCH=%{python3_sitearch}
%cmake_build
%__cmake --build %{__cmake_builddir} --target doc
%install
%cmake_install
%ldconfig_scriptlets
%ldconfig_scriptlets -n libpamtest
%oreon_autofiles libpamtest usr/*/lib*.so.*
%oreon_autofiles libpamtest-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libpamtest-doc usr/*/lib*.so.*
%oreon_autofiles python3-libpamtest usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libpamtest -f %{oreon_filedir}/libpamtest.list
%files -n libpamtest-devel -f %{oreon_filedir}/libpamtest-devel.list
%files -n libpamtest-doc -f %{oreon_filedir}/libpamtest-doc.list
%files -n python3-libpamtest -f %{oreon_filedir}/python3-libpamtest.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.8-1
- Prepare for Oreon 11 (RP1)
