%global source1_hash 2af9e7ab3f24f1b4c0ec753a788c6ba588460d80f1ef852df23e1dfa2575e0ec
%global source0_hash 6c8a2148a7b85043b68492bce43316b0e2e214fc4e628c7ede078e76e216330b
%global source2_key_fpr 259B3792B3D6D319212CC4DCD5BF9FEB0313653A
Summary:        Utilities for managing filesystem extended attributes
Name: attr
Version: 2.6.0
Release:        1%{?dist}
Source0:        https://download.savannah.nongnu.org/releases/attr/attr-%{version}.tar.xz
Source1:        https://download.savannah.nongnu.org/releases/attr/attr-%{version}.tar.xz.sig
Source2: agruen-key.gpg
Patch3:  0003-attr-2.4.48-xattr-conf-nfs4-acls.patch
License: GPL-2.0-or-later
URL: https://savannah.nongnu.org/projects/attr
Requires: libattr%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(FileHandle)
# /oreon:deps
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
Requires: glibc-headers
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

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
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
rm -f $RPM_BUILD_ROOT%{_libdir}/libattr.{l,}a
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}*
ln -fs ../sys/xattr.h $RPM_BUILD_ROOT%{_includedir}/attr/xattr.h
%find_lang %{name}
%ldconfig_scriptlets -n libattr
%oreon_autofiles libattr usr/*/lib*.so.*
%oreon_autofiles libattr-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libattr -f %{oreon_filedir}/libattr.list
%files -n libattr-devel -f %{oreon_filedir}/libattr-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.2-8
- Prepare for Oreon 11 (RP1)
