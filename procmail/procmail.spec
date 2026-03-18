# hardened build if not overridden
%{!?_hardened_build:%global _hardened_build 1}

%if %{?_hardened_build}%{!?_hardened_build:0}
%global hardened_flags -pie -Wl,-z,relro,-z,now
%endif

Summary: Mail processing program
Name: procmail
Version: 3.24
Release: 10%{?dist}
# Dual licensed "gpl-2.0-or-later OR artistic-perl-1.0", but
# artistic-perl-1.0 is not allowed, thus dropped from the license
# tag as per: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/423
License: gpl-2.0-or-later
URL: https://github.com/BuGlessRB/%{name}
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
# Source2: http://www.linux.org.uk/~telsa/BitsAndPieces/procmailrc
# The Telsa config file doesn't seem to be available anymore, using local copy
Source2: procmailrc
Patch0: procmail-3.24-rhconfig.patch
Patch1: procmail-3.15.1-man.patch
Patch2: procmail-3.22-truncate.patch
Patch3: procmail-3.24-ipv6.patch
Patch4: procmail-3.24-coverity-scan-fixes.patch
# https://github.com/BuGlessRB/procmail/pull/7
Patch5: procmail-3.24-gcc-14-fix.patch
BuildRequires: make
BuildRequires: gcc

%description
Procmail can be used to create mail-servers, mailing lists, sort your
incoming mail into separate folders/files (real convenient when subscribing
to one or more mailing lists or for prioritising your mail), preprocess
your mail, start any programs upon mail arrival (e.g. to generate different
chimes on your workstation for different types of mail) or selectively
forward certain incoming mail automatically to someone.

%prep
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


%files
%doc Artistic COPYING FAQ FEATURES HISTORY README KNOWN_BUGS examples telsas_procmailrc

%{_bindir}/formail
%attr(2755,root,mail) %{_bindir}/lockfile
%{_bindir}/mailstat
%attr(0755,root,mail) %{_bindir}/procmail

%{_mandir}/man[15]/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.24-10
- Prepare for Oreon 11 (RP1)
