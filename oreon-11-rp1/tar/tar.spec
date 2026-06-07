%global source0_hash none

%bcond_without selinux
# Don't run check on 32-bit arches, seems to be issues with some tests
%ifarch %{ix86} %{arm}
%bcond_with check
%else
%bcond_without check
%endif

Summary: GNU file archiving program
Name: tar
Epoch: 2
Version: 1.35
Release: 8%{?dist}
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/tar/

Source0:        https://mirrors.kernel.org/gnu/tar/tar-%{version}.tar.xz
Source1:        https://mirrors.kernel.org/gnu/tar/tar-%{version}.tar.xz.sig

# Note that all patches are documented in patch files (git format-patch format)
Patch1:  tar-1.28-loneZeroWarning.patch
Patch2:  tar-1.28-vfatTruncate.patch
Patch3:  tar-1.29-wildcards.patch
Patch4:  tar-1.28-atime-rofs.patch
Patch9:  tar-1.28-document-exclude-mistakes.patch
Patch10: tar-1.33-fix-capabilities-test.patch
Patch11: tar-1.35-padding-zeros.patch
Patch12: tar-1.30-disk-read-error.patch
Patch13: tar-1.35-fix-spurious-diagnostic-during-extraction-of-.-with-keep-newer-files.patch
Patch14: tar-1.35-add-forgotten-tests-from-upstream.patch
Patch15: tar-1.35-revert-fix-savannah-bug-633567.patch
# Source: https://cgit.git.savannah.gnu.org/cgit/tar.git/diff/?id=5114218025b4562392dd260e2533d3fa2bc0220e
Patch16: tar-1.35-Fix-Savane-bug-64581.patch
# Source: https://cgit.git.savannah.gnu.org/cgit/tar.git/diff/?id=4e742fc8674064a9fa00d4483d06aca48d5b0463
Patch22: tar-1.35-no-overwrite-dir-no-overwrite-even-temporarily.patch
#tar commits from upstream
# 56fb4a96ca43c247261b8c04dd65592f990f98ac
# 7c241126f14975c7f5df4268b434f276fc7f8842
# bdd773d028cd21f9b76b8cc306c57e0db3607e82
# cdb586803b762d9021db2ae8bf5dad3f9b8e4f77
# 915a8077af12a3eaf7800dbb1a4259783d9933ca
# 8fca2d35e88d10f0ddcb36720e88f40ac57f67f0
# e1445cfdf0dfd2f792532afc1eb18b01523dbfb4
# 75b03fdff48916bd0654677ed21379bdb0db016d
# 8767b1c84a910cce562059abad5bbf14e72434a0
#Gnulib commits from upstream to bring openat2 support
# 0b97ffdf32bdab909d02449043447237273df75e
# c706216fec5a509bf9b1214892de01aa9303ade0
# c6502cda83752ff2235d2064c213e7a9e2214201
# 5746cd1cdbb2caf0e321ea79041885fc7ef22423
# 3d23c8df2582a6b0e44e048d431ecb00a14667ec
# a209366ed34eca8ede481ec1b1c4e22f614c448d
# 8e85114bf1d51d9ea54a89f058c3a2cfa0c19c5e
# 6bff6c3741209e933e721e81e1b5c5abdbd4389a
# 24d2acd301cea7cde1928c84f926a54707e945d5
# 4e1fa851f4f43f749d18b83500757f5bcf1f47bd
# 20074698382b7e4f049f52bbdeaf6a39508a8601
# d1aeb7388926e045bdec0f7934c5522c4745f02c
# 45b6e6898d1f931bfca41d961289bd6ac33238e5
Patch23: tar-1.35-CVE-2025-45582.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: libacl-devel
BuildRequires: make
BuildRequires: texinfo

%if %{with check}
# cover needs of tar's testsuite
BuildRequires: attr acl policycoreutils
%endif

%if %{with selinux}
BuildRequires: libselinux-devel
%endif
Provides: bundled(gnulib)
Provides: bundled(paxutils)
Provides: /bin/tar
Provides: /bin/gtar

%description
The GNU tar program saves many files together in one archive and can
restore individual files (or all of the files) from that archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive. Tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives, and the ability to perform incremental and full
backups.

If you want to use tar for remote backups, you also need to install
the rmt package on the remote box.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
autoreconf -v

# Keep only entries related to the latest release.
mv ChangeLog{,~}
awk 'stop = false; /^2014-07-27/ { stop = true; exit }; { print }' \
    < ChangeLog~ > ChangeLog


%build
%configure \
    %{!?with_selinux:--without-selinux} \
    --with-lzma="xz --format=lzma" \
    DEFAULT_RMT_DIR=%{_sysconfdir} \
    RSH=/usr/bin/ssh

%make_build


%install
%make_install

ln -s tar $RPM_BUILD_ROOT%{_bindir}/gtar
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
ln -s tar.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/gtar.1

# XXX Nuke unpackaged files.
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/rmt
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/rmt.8*

%find_lang %name


%check
%if %{with check}
rm -f $RPM_BUILD_ROOT/test/testsuite
# make check TESTSUITEFLAGS='-k \!dirrem01,\!dirrem02' || (
make check || (
    # get the error log
    set +x
    find -name testsuite.log | while read line; do
        echo "=== $line ==="
        cat "$line"
        echo
    done
    false
)
%endif


%files -f %{name}.lang
%license COPYING
%doc AUTHORS README THANKS NEWS ChangeLog
%{_bindir}/tar
%{_bindir}/gtar
%{_mandir}/man1/tar.1*
%{_mandir}/man1/gtar.1*
%{_infodir}/tar.info*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.35-8
- Prepare for Oreon 11 (RP1)
