%global source0_hash 1e45f80c03b64faf2511ddd4053a04e7a8bcf653f1b9f67e4841c346002613e5
Name:           perl-Sys-Syscall
Version:        0.25
Release:        1%{?dist}
Summary:        Access system calls that Perl doesn't normally provide access to
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-Syscall
Source0:        https://cpan.metacpan.org/modules/by-module/Sys/Sys-Syscall-%{version}.tar.gz
Patch0:         Sys-Syscall-0.25-Add-ppc64le-support.patch
Patch1:         Sys-Syscall-0.25-Add-s390-x-support.patch
Patch2:         Sys-Syscall-0.25-Add-aarch64-support.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Use epoll, sendfile, from Perl. Mostly Linux-only support now, but more
syscalls/OSes planned for future.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sys-Syscall-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
rm -v %{buildroot}%{_mandir}/man3/Sys::README.3pm || :
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
