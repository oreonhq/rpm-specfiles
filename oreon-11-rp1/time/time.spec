%global source1_hash 7553b491501346605b9b6e7ee564495dd3f00e3d1f8def02f086c9dd1db85b3a
%global source0_hash fbacf0c81e62429df3e33bda4cee38756604f18e01d977338e23306a3e3b521e
%global source2_key_fpr F576AAAC1B0FF849792D8CB129A794FD2272BC86
Summary:        A GNU utility for monitoring a program's use of system resources
Name:       time
Version:    1.9
Release:        1%{?dist}
License:    GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later
SourceLicense: %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Texinfo-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-1.0-or-later AND X11 AND FSFAP AND FSFUL AND FSFULLR AND LicenseRef-Fedora-Public-Domain
Url:        https://www.gnu.org/software/%{name}/
Source0:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-F576AAAC1B0FF849792D8CB129A794FD2272BC86.gpg
Patch0:        time-1.8-Prefer-clock_gettime-CLOCK_MONOTONIC.patch
Patch1:        time-1.9-Improve-info-directory-index-entry-description.patch
Patch2:        time-1.9-Use-kibibytes-instead-of-kilobytes-in-a-documentatio.patch
Patch3:        time-1.9-Close-outfp-before-exec.patch
Patch4:        time-1.9-drop-flawed-rss-test.patch
Patch5:        time-1.9-Fix-formatting-a-trailing-backslash-and-a-percent-si.patch
Patch6:        time-1.9-Fix-compiling-with-GCC15.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  texinfo
# /oreon:deps
%description
The GNU time utility runs another program, collects information about
the resources used by that program while it is running, and displays
the results.

%prep

test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# Set time stamp stored in an info page to the latest patch
touch -d "$(sed -n -e '/^Date: /{s/^[^:]*: //;p}' %{PATCH2})" doc/time.texi
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
# Correct version VERSION flag for doc/time.texi
# <https://lists.gnu.org/archive/html/bug-time/2021-01/msg00000.html>
printf '%{version}\n' > .tarball-version
autoreconf -fi

%build

%configure
%{make_build}
%install
%{make_install}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%oreon_autofiles main

%check

%{make_build} check
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9-28
- Prepare for Oreon 11 (RP1)
