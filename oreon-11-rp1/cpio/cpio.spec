%global source2_hash a42435ade567df0678f7c6ba9d09af426aedff38d87b5fc0f67737ccea6b5fd2
%global source0_hash 937610b97c329a1ec9268553fb780037bcfff0dcffe9725ebc4fd9c1aa9075db
%global source3_key_fpr 325F650C4C2B6AD58807327A3602B07F55D0C732
Summary:        A GNU archiving program
Name: cpio
Version: 2.15
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/cpio/
Source0:        https://mirrors.kernel.org/gnu/cpio/cpio-%{version}.tar.bz2
Source1: cpio.1
Source2:        https://mirrors.kernel.org/gnu/cpio/cpio-%{version}.tar.bz2.sig
Source3: gray-key.gpg
Patch1: cpio-2.14-rh.patch
Patch2: cpio-2.14-exitCode.patch
Patch3: cpio-2.14-dev_number.patch
Patch4: cpio-2.9.90-defaultremoteshell.patch
Patch5: cpio-2.14-patternnamesigsegv.patch
Patch7: cpio-2.10-longnames-split.patch
Patch8: cpio-2.11-crc-fips-nit.patch
Provides: bundled(gnulib)
Provides: bundled(paxutils)
Provides: /bin/cpio
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
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

test -z "%{source3_key_fpr}" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source3_key_fpr}" || { echo "oreon: Source3 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE2}' --data='%{SOURCE0}'
%autosetup -p1

%build

autoreconf -fi
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
%oreon_autofiles main

%check

rm -f ${RPM_BUILD_ROOT}/test/testsuite
make check || {
    echo "### TESTSUITE.LOG ###"
    cat tests/testsuite.log
    exit 1
}
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.15-9
- Prepare for Oreon 11 (RP1)
