%global source1_hash c4932271b3c79e303cc0fa92b8345c04e236f35499a45b1c4e6793713c497298
%global source0_hash 4d62ff37342ec7aed748535323930c7cf94acf71c3591882b26a7ea50f3edc16
%bcond_without selinux
%ifarch %{ix86} %{arm}
%bcond_with check
%else
%bcond_without check
%endif
Summary:        GNU file archiving program
Name: tar
Epoch: 2
Version: 1.35
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/tar/
Source0:        https://mirrors.kernel.org/gnu/tar/tar-%{version}.tar.xz
Source1:        https://mirrors.kernel.org/gnu/tar/tar-%{version}.tar.xz.sig
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
Patch16: tar-1.35-Fix-Savane-bug-64581.patch
Patch22: tar-1.35-no-overwrite-dir-no-overwrite-even-temporarily.patch
Patch23: tar-1.35-CVE-2025-45582.patch
%if %{with check}
%endif
%if %{with selinux}
%endif
Provides: bundled(gnulib)
Provides: bundled(paxutils)
Provides: /bin/tar
Provides: /bin/gtar
# oreon:deps
BuildRequires:  acl
BuildRequires:  attr
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libacl-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  policycoreutils
BuildRequires:  texinfo
# /oreon:deps
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
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/rmt
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/rmt.8*
%find_lang %name
%oreon_autofiles main

%check

%if %{with check}
rm -f $RPM_BUILD_ROOT/test/testsuite
make check || (
    set +x
    find -name testsuite.log | while read line; do
        echo "=== $line ==="
        cat "$line"
        echo
    done
    false
)
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.35-8
- Prepare for Oreon 11 (RP1)
