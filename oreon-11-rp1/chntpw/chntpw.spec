%global source0_hash 96e20905443e24cba2f21e51162df71dd993a1c02bfa12b1be2d0801a4ee2ccc

Name:           chntpw
# Version is taken from HISTORY.txt
Version:        1.00
Release:        22.140201%{?dist}
Summary:        Change passwords in Windows SAM files
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://pogostick.net/~pnh/ntpasswd/
Source0:        http://pogostick.net/~pnh/ntpasswd/chntpw-source-140201.zip
Source2:        chntpw-README.Dist
# The man pages are borrowed from Debian
Source10:       chntpw.8
Source11:       reged.8
Source12:       sampasswd.8
Source13:       samusrgrp.8

BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires: make

# Patches sent upstream on 2009-06-08.
Patch1:         chntpw-140201-get_abs_path.patch

Patch3:         chntpw-140201-port-to-gcrypt-debian.patch

# Patches from Jim Meyering to improve robustness of the code.
Patch4:         chntpw-110511-robustness.patch
Patch5:         chntpw-080526-correct-test-for-failing-open-syscall.patch
Patch6:         chntpw-110511-detect-failure-to-write-key.patch
Patch7:         chntpw-110511-reged-no-deref-null.patch

Patch8:         chntpw-140201-fix-bogus-errno-use.patch

# Cast around new GCC error for mismatched pointer arguments
Patch9:         chntpw-140201-hexdump-pointer-type.patch

%description
This is a utility to (re)set the password of any user that has a valid
(local) account on your Windows NT/2k/XP/Vista etc system. You do not
need to know the old password to set a new one. It works offline, that
is, you have to shutdown your computer and boot off a floppy disk or CD
or another system. Will detect and offer to unlock locked or disabled
out user accounts! There is also a registry editor and other registry
utilities that works under Linux/Unix, and can be used for other things
than password editing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-140201
cp -p %{SOURCE2} README.Dist
sed -e 's/\r$//' WinReg.txt > WinReg.txt.eol
touch -c -r WinReg.txt WinReg.txt.eol
mv WinReg.txt.eol WinReg.txt

%patch -P1 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1

%build
make CC="%__cc" EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
    chntpw cpnt reged sampasswd samusrgrp

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp chntpw cpnt reged sampasswd samusrgrp $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8/
cp -p %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} \
    $RPM_BUILD_ROOT%{_mandir}/man8/

%files
%doc GPL.txt LGPL.txt README.txt regedit.txt WinReg.txt HISTORY.txt
%doc README.Dist
%{_bindir}/chntpw
%{_bindir}/cpnt
%{_bindir}/reged
%{_bindir}/sampasswd
%{_bindir}/samusrgrp
%{_mandir}/man8/*.8*

%changelog
%autochangelog
