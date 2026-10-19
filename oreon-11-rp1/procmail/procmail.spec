%global source0_hash 514ea433339783e95df9321e794771e4887b9823ac55fdb2469702cf69bd3989
%{!?_hardened_build:%global _hardened_build 1}
%if %{?_hardened_build}%{!?_hardened_build:0}
%global hardened_flags -pie -Wl,-z,relro,-z,now
%endif
Summary:        Mail processing program
Name: procmail
Version: 3.24
Release:        1%{?dist}
License: gpl-2.0-or-later
URL: https://github.com/BuGlessRB/%{name}
Source0:        https://github.com/BuGlessRB/procmail/archive/refs/tags/v3.24.tar.gz#/procmail-3.24.tar.gz
Source2: procmailrc
Patch0: procmail-3.24-rhconfig.patch
Patch1: procmail-3.15.1-man.patch
Patch2: procmail-3.22-truncate.patch
Patch3: procmail-3.24-ipv6.patch
Patch4: procmail-3.24-coverity-scan-fixes.patch
Patch5: procmail-3.24-gcc-14-fix.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Procmail can be used to create mail-servers, mailing lists, sort your
incoming mail into separate folders/files (real convenient when subscribing
to one or more mailing lists or for prioritising your mail), preprocess
your mail, start any programs upon mail arrival (e.g. to generate different
chimes on your workstation for different types of mail) or selectively
forward certain incoming mail automatically to someone.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

find examples -type f | xargs chmod 644

%build

make RPM_OPT_FLAGS="$(getconf LFS_CFLAGS) -std=gnu89" autoconf.h
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS %{?hardened_flags} -Wno-comments $(getconf LFS_CFLAGS) -std=gnu89"
%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,5}
make \
    BASENAME=${RPM_BUILD_ROOT}%{_prefix} MANDIR=${RPM_BUILD_ROOT}%{_mandir} \
    install
cp -p %{SOURCE2} telsas_procmailrc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.24-10
- Prepare for Oreon 11 (RP1)
