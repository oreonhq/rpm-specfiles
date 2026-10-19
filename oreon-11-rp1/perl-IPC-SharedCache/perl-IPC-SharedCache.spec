%global source0_hash 21976aa502da5b0d1883ca8a733672fd43739c41f8544b4e9261306c52656c6d
Name:           perl-IPC-SharedCache
Version:        1.3
Release:        58%{?dist}
Summary:        Perl module to manage a cache in SysV IPC shared memory
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/IPC-SharedCache
Source0:        https://cpan.metacpan.org/modules/by-module/IPC/IPC-SharedCache-%{version}.tar.gz
Patch0:         IPC-SharedCache-1.3-test.patch
BuildArch:      noarch
Requires:       perl(IPC::ShareLite) >= 0.06
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IPC::ShareLite\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IPC::ShareLite)
BuildRequires:  perl(Storable)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a shared memory cache accessed as a tied hash.
Shared memory is an area of memory that is available to all processes.
It is accessed by choosing a key, the ipc_key argument to tie.  Every
process that accesses shared memory with the same key gets access to
the same region of memory.  In some ways it resembles a file system,
but it is not hierarchical and it is resident in memory.  This makes
it harder to use than a filesystem but much faster.  The data in
shared memory persists until the machine is rebooted or it is
explicitly deleted.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPC-SharedCache-%{version}

# Debian patch for tests, which fixes problem of HTML::Template
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
