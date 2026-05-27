%global source0_hash 937610b97c329a1ec9268553fb780037bcfff0dcffe9725ebc4fd9c1aa9075db

Summary: A GNU archiving program
Name: cpio
Version: 2.15
Release: 9%{?dist}
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/cpio/
Source0: https://ftp.gnu.org/gnu/cpio/cpio-%{version}.tar.bz2

# help2man generated manual page distributed only in RHEL/Fedora
Source1: cpio.1

Source2: https://ftp.gnu.org/gnu/cpio/cpio-%{version}.tar.bz2.sig
# https://savannah.gnu.org/projects/cpio/ lists one maintainer, gray
# and their GPG key is https://savannah.gnu.org/people/viewgpg.php?user_id=311
Source3: gray-key.gpg

# We use SVR4 portable format as default.
Patch1: cpio-2.14-rh.patch

# fix warn_if_file_changed() and set exit code to 1 when cpio fails to store
# file > 4GB (#183224)
# http://lists.gnu.org/archive/html/bug-cpio/2006-11/msg00000.html
Patch2: cpio-2.14-exitCode.patch

# Support major/minor device numbers over 127 (bz#450109)
# http://lists.gnu.org/archive/html/bug-cpio/2008-07/msg00000.html
Patch3: cpio-2.14-dev_number.patch

# Define default remote shell as /usr/bin/ssh (#452904)
Patch4: cpio-2.9.90-defaultremoteshell.patch

# Fix segfault with nonexisting file with patternnames (#567022)
# http://savannah.gnu.org/bugs/index.php?28954
# We have slightly different solution than upstream.
Patch5: cpio-2.14-patternnamesigsegv.patch

# Fix bad file name splitting while creating ustar archive (#866467)
# (fix backported from tar's source)
Patch7: cpio-2.10-longnames-split.patch

# Cpio does Sum32 checksum, not CRC (downstream)
Patch8: cpio-2.11-crc-fips-nit.patch

Provides: bundled(gnulib)
Provides: bundled(paxutils)
Provides: /bin/cpio
BuildRequires: gcc
BuildRequires: texinfo, autoconf, automake, gettext, gettext-devel
BuildRequires: make
BuildRequires: gnupg2

%description
GNU cpio copies files into or out of a cpio or tar archive.  Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions.  The archive can be another file on the disk, a magnetic
tape, or a pipe.  GNU cpio supports the following archive formats:  binary,
old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar and POSIX.1
tar.  By default, cpio creates binary format archives, so that they are
compatible with older cpio programs.  When it is extracting files from
archives, cpio automatically recognizes which kind of archive it is reading
and can read archives created on machines with a different byte-order.

Install cpio if you need a program to manage file archives.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE2}' --data='%{SOURCE0}'
%autosetup -p1


%build
autoreconf -fi
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=118112
CFLAGS="$RPM_OPT_FLAGS -std=gnu17"
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE -pedantic -fno-strict-aliasing -Wall $CFLAGS"
%configure --with-rmt="%{_sysconfdir}/rmt"
%make_build
(cd po && make update-gmo)


%install
%make_install

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/*.1*
install -c -p -m 0644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_mandir}/man1

%find_lang %{name}

%check
rm -f ${RPM_BUILD_ROOT}/test/testsuite
make check || {
    echo "### TESTSUITE.LOG ###"
    cat tests/testsuite.log
    exit 1
}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man*/*
%{_infodir}/*.info*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.15-9
- Prepare for Oreon 11 (RP1)
