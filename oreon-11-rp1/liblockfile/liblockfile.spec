%global source0_hash none

Name:           liblockfile
Version:        1.17
Release:        12%{?dist}
Summary:        This implements a number of functions found in -lmail on SysV systems

# regarding license please see file COPYRIGHT
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://packages.qa.debian.org/libl/liblockfile.html
Source0:        https://deb.debian.org/debian/pool/main/libl/liblockfile/liblockfile_%{version}.orig.tar.gz

BuildRequires:  gcc
BuildRequires: make

%description
This library implements a number of functions found in -lmail on SysV
systems. These functions are designed to lock the standard mailboxes in
/var/mail (or wherever the system puts them).

In additions, this library adds a number of functions to create,
manage and remove generic lockfiles.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{VERSION}

# There are occurrences of "install -g GROUP ...".
#
# Changing the group requires permissions that are normally not
# available while packaging.
#
# Let's remove "-g GROUP".
sed -Ei "/install/ s/-g [^ ]+//" Makefile.in

# Makefile.in mixes and messes with DESTDIR and prefix.
# See the following pull requests submitted upstream:
# https://github.com/miquels/liblockfile/pull/11
# https://github.com/miquels/liblockfile/pull/15
sed -i \
    -e '/^prefix/s,\$(DESTDIR),,' \
    -e 's,\(\$(\(lib\|include\|man\|nfslock\|bin\)dir)\),$(DESTDIR)\1,' \
    -e '/-DLOCKPROG/s,\$(DESTDIR),,' Makefile.in

%build
%configure --enable-shared --with-mailgroup
%make_build

%install
%make_install

ldconfig -N -n %{buildroot}/%{_libdir}

%ldconfig_scriptlets

%files
%attr(2755,root,mail) %{_bindir}/dotlockfile
%{_libdir}/liblockfile.so.1.0
%{_libdir}/liblockfile.so.1
%{_mandir}/man1/dotlockfile.1*
%doc README COPYRIGHT Changelog


%files devel
%{_libdir}/liblockfile.so
%{_includedir}/maillock.h
%{_includedir}/lockfile.h
%{_libdir}/liblockfile.a
%{_mandir}/man3/lockfile_create.3*
%{_mandir}/man3/maillock.3*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17-12
- Import
