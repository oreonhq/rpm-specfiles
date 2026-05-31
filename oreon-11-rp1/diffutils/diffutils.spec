%global source0_hash 7c8b7f9fc8609141fdea9cece85249d308624391ff61dedaf528fcb337727dfd

Summary: GNU collection of diff utilities
Name: diffutils
Version: 3.12
Release: 5%{?dist}
URL: https://www.gnu.org/software/diffutils/diffutils.html
Source:        https://ftp.gnu.org/gnu/diffutils/diffutils-%{version}.tar.xz
# upstream fixes
# cross compile build of 3.12 diffutils fails
Patch: diffutils-3.12-cross-compiler-build-fail.patch
# sdiff: continue → break
Patch: diffutils-3.12-sdiff-continue-break.patch
# sdiff: pacify gcc -flto -Wmaybe-uninitialized
Patch: 0001-sdiff-pacify-gcc-flto-Wmaybe-uninitialized.patch
# sdiff: port back to C17
Patch: 0001-sdiff-port-back-to-C17.patch
License: GPL-3.0-or-later
Provides: bundled(gnulib)
BuildRequires: gcc
BuildRequires: help2man
BuildRequires: autoconf, automake, texinfo
BuildRequires: make

%description
Diffutils includes four utilities: diff, cmp, diff3 and sdiff. Diff
compares two files and shows the differences, line by line.  The cmp
command shows the offset and line numbers where two files differ, or
cmp can show the characters that differ between the two files.  The
diff3 command shows the differences between three files.  Diff3 can be
used when two people have made independent changes to a common
original; diff3 can produce a merged file that contains both sets of
changes and warnings about conflicts.  The sdiff command can be used
to merge two files interactively.

Install diffutils if you need to compare text files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Run autoreconf for aarch64 support (bug #925256).
autoreconf

%build
%configure
make PR_PROGRAM=%{_bindir}/pr

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%find_lang %{name}

%check
# Disable update-copyright gnulib test (bug #1239428).
>gnulib-tests/test-update-copyright.sh
make check

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/diffutils.info*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12-5
- Prepare for Oreon 11 (RP1)
