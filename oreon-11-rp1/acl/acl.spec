%global source0_hash none

%global source2_key_fpr B902B5271325F892AC251AD441633B9FE837F581

Summary: Access control list utilities
Name: acl
Version: 2.3.2
Release: 6%{?dist}
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: libattr-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: perl(FileHandle)
BuildRequires: gnupg2
Requires: libacl%{?_isa} = %{version}-%{release}
Source0:        https://download-mirror.savannah.gnu.org/releases/acl/acl-%{version}.tar.gz
Source1:        https://download-mirror.savannah.gnu.org/releases/acl/acl-%{version}.tar.gz.sig
# Retreived from https://savannah.nongnu.org/people/viewgpg.php?user_id=15000
# Source2: agruen-key.gpg
# Retrieved from https://savannah.nongnu.org/people/viewgpg.php?user_id=42032
Source2: vapier-key.gpg

# avoid permission denied problem with LD_PRELOAD in the test-suite
Patch1: 0001-acl-2.2.53-test-runwrapper.patch

License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://savannah.nongnu.org/projects/acl

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
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure

# uncomment to turn on optimizations
# sed -i 's/-O2/-O0/' libtool include/builddefs
# unset CFLAGS

%make_build

%check
# make the test-suite use the just built library (instead of the system one)
export LD_LIBRARY_PATH="${RPM_BUILD_ROOT}%{_libdir}:${LD_LIBRARY_PATH}"

if ./setfacl -m "u:$(id -u):rwx" .; then
    if test 0 = "$(id -u)"; then
        # test/root/permissions.test requires the 'daemon' user to be a member
        # of the 'bin' group in order not to fail.  Prevent the test from
        # running if we detect that its requirements are not met (#1085389).
        if id -nG daemon | { ! grep bin >/dev/null; }; then
            sed -e 's|test/root/permissions.test||' \
                -i test/Makemodule.am Makefile.in Makefile
        fi

        # test/root/setfacl.test fails if 'bin' user cannot access build dir
        if ! runuser -u bin -- "${PWD}/setfacl" --version; then
            sed -e 's|test/root/setfacl.test||' \
                -i test/Makemodule.am Makefile.in Makefile
        fi
    fi

    # run the upstream test-suite
    %make_build check || exit $?
else
    echo '*** ACLs are probably not supported by the file system,' \
         'the test-suite will NOT run ***'
fi

%install
%make_install

# get rid of libacl.a and libacl.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libacl.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libacl.la

chmod 0755 $RPM_BUILD_ROOT/%{_libdir}/libacl.so.*.*.*

# drop already installed documentation, we will use an RPM macro to install it
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}*

%find_lang %{name}

%ldconfig_scriptlets -n libacl

%files -f %{name}.lang
%license doc/COPYING*
%{_bindir}/chacl
%{_bindir}/getfacl
%{_bindir}/setfacl
%{_mandir}/man1/chacl.1*
%{_mandir}/man1/getfacl.1*
%{_mandir}/man1/setfacl.1*
%{_mandir}/man5/acl.5*

%files -n libacl-devel
%{_libdir}/libacl.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/acl
%{_includedir}/sys/acl.h
%{_mandir}/man3/acl_*

%files -n libacl
%{_libdir}/libacl.so.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.2-6
- Prepare for Oreon 11 (RP1)
