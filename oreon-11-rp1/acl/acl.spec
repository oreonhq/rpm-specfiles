%global source1_hash dbe12b8f58dd600b14d7bfd57c378e4f792f09a11d96d40e604d80bb926a6fd5
%global source0_hash 73c853c3d44e1f693e5a96a986f1bd19d3d0dac2c7d453e796177774bc4e5f6a
%global source2_key_fpr 259B3792B3D6D319212CC4DCD5BF9FEB0313653A
Summary:        Access control list utilities
Name: acl
Version: 2.4.0
Release:        1%{?dist}
Requires: libacl%{?_isa} = %{version}-%{release}
Source0:        https://download-mirror.savannah.gnu.org/releases/acl/acl-%{version}.tar.gz
Source1:        https://download-mirror.savannah.gnu.org/releases/acl/acl-%{version}.tar.gz.sig
Source2: agruen-key.gpg
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://savannah.nongnu.org/projects/acl
# oreon:deps
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(FileHandle)
# /oreon:deps
%description
This package contains the getfacl and setfacl utilities needed for
manipulating access control lists.

%package -n libacl
Summary: Dynamic library for access control list support
License: LGPL-2.1-or-later
Conflicts: filesystem < 3
%description -n libacl
This package contains the libacl.so dynamic library which contains
the POSIX 1003.1e draft standard 17 functions for manipulating access
control lists.

%package -n libacl-devel
Summary: Files needed for building programs with libacl
License: LGPL-2.1-or-later
Requires: libacl%{?_isa} = %{version}-%{release}, libattr-devel
%description -n libacl-devel
This package contains header files and documentation needed to develop
programs which make use of the access control list programming interface
defined in POSIX 1003.1e draft standard 17.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%configure
%make_build
%check

export LD_LIBRARY_PATH="${RPM_BUILD_ROOT}%{_libdir}:${LD_LIBRARY_PATH}"
if ./setfacl -m "u:$(id -u):rwx" .; then
    if test 0 = "$(id -u)"; then
        if id -nG daemon | { ! grep bin >/dev/null; }; then
            sed -e 's|test/root/permissions.test||' \
                -i test/Makemodule.am Makefile.in Makefile
        fi
        if ! runuser -u bin -- "${PWD}/setfacl" --version; then
            sed -e 's|test/root/setfacl.test||' \
                -i test/Makemodule.am Makefile.in Makefile
        fi
    fi
    %make_build check || exit $?
else
    echo '*** ACLs are probably not supported by the file system,' \
         'the test-suite will NOT run ***'
fi
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libacl.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libacl.la
chmod 0755 $RPM_BUILD_ROOT/%{_libdir}/libacl.so.*.*.*
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}*
%find_lang %{name}
%ldconfig_scriptlets -n libacl
%oreon_autofiles libacl usr/*/lib*.so.*
%oreon_autofiles libacl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libacl -f %{oreon_filedir}/libacl.list
%files -n libacl-devel -f %{oreon_filedir}/libacl-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.2-6
- Prepare for Oreon 11 (RP1)
