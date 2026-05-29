%global source0_hash f2e97b0ab7ce293681ab701915766190d607a1dba7fae8a718138150b700a70b

Summary: Utilities for managing filesystem extended attributes
Name: attr
Version: 2.5.2
Release: 8%{?dist}
Source0:        https://download.savannah.nongnu.org/releases/attr/attr-2.5.2.tar.xz
Source1:        https://download.savannah.nongnu.org/releases/attr/attr-2.5.2.tar.xz.sig
# Retreived from https://savannah.nongnu.org/people/viewgpg.php?user_id=15000
# Source2: agruen-key.gpg
# Retrieved from https://savannah.nongnu.org/people/viewgpg.php?user_id=42032
Source2: vapier-key.gpg

# xattr.conf: remove entries for NFSv4 ACLs namespaces (#1031423)
# https://lists.nongnu.org/archive/html/acl-devel/2019-03/msg00000.html
# https://lists.nongnu.org/archive/html/acl-devel/2019-03/msg00001.html
# https://lists.nongnu.org/archive/html/acl-devel/2019-05/msg00000.html
Patch3:  0003-attr-2.4.48-xattr-conf-nfs4-acls.patch

License: GPL-2.0-or-later
URL: https://savannah.nongnu.org/projects/attr
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: make
BuildRequires: gnupg2
Requires: libattr%{?_isa} = %{version}-%{release}

# needed for %%check
BuildRequires: perl(FileHandle)

%description
A set of tools for manipulating extended attributes on filesystem
objects, in particular getfattr(1) and setfattr(1).
An attr(1) command is also provided which is largely compatible
with the SGI IRIX tool of the same name.

%package -n libattr
Summary: Dynamic library for extended attribute support
License: LGPL-2.1-or-later
Conflicts: filesystem < 3

%description -n libattr
This package contains the libattr.so dynamic library which contains
the extended attribute system calls and library functions.

%package -n libattr-devel
Summary: Files needed for building programs with libattr
License: LGPL-2.1-or-later
Requires: libattr%{?_isa} = %{version}-%{release}

# for <sys/xattr.h> which <attr/xattr.h> is symlinked to
Requires: glibc-headers

# provides {,f,l}{get,list,remove,set}xattr.2 man pages
Recommends: man-pages

%description -n libattr-devel
This package contains header files and documentation needed to
develop programs which make use of extended attributes.
For Linux programs, the documented system call API is the
recommended interface, but an SGI IRIX compatibility interface
is also provided.

Currently only ext2, ext3, ext4 and XFS support extended attributes.
The SGI IRIX compatibility API built above the Linux system calls is
used by programs such as xfsdump(8), xfsrestore(8) and xfs_fsr(8).

You should install libattr-devel if you want to develop programs
which make use of extended attributes.  If you install libattr-devel,
you'll also want to install attr.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# FIXME: root tests are not ready for SELinux
sed -e 's|test/root/getfattr.test||' \
    -i test/Makemodule.am Makefile.in

%build
%configure
%make_build -C po ka.gmo
%make_build

%check
if ./setfattr -n user.name -v value .; then
    make check || exit $?
else
    echo '*** xattrs are probably not supported by the file system,' \
         'the test-suite will NOT run ***'
fi

%install
%make_install

# get rid of libattr.a and libattr.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libattr.{l,}a

# drop already installed documentation, we will use an RPM macro to install it
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}*

# temporarily provide attr/xattr.h symlink until users are migrated (#1601482)
ln -fs ../sys/xattr.h $RPM_BUILD_ROOT%{_includedir}/attr/xattr.h

%find_lang %{name}

%ldconfig_scriptlets -n libattr

%files -f %{name}.lang
%doc doc/CHANGES
%license doc/COPYING*
%{_bindir}/attr
%{_bindir}/getfattr
%{_bindir}/setfattr
%{_mandir}/man1/attr.1*
%{_mandir}/man1/getfattr.1*
%{_mandir}/man1/setfattr.1*

%files -n libattr-devel
%{_libdir}/libattr.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/attr
%{_mandir}/man3/attr_*.3.*

%files -n libattr
%{_libdir}/libattr.so.*
%config(noreplace) %{_sysconfdir}/xattr.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.2-8
- Prepare for Oreon 11 (RP1)
