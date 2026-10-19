%global source0_hash b6da746853253d5b4ac43191b4f69a4719595ee13a7ca676a8054cf36e6d16bb
%{bcond_with perl_IO_Socket_INET6_enables_optional_test}
Name:           perl-IO-Socket-INET6
Version:        2.73
Release:        12%{?dist}
Summary:        Perl Object interface for AF_INET|AF_INET6 domain sockets
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Socket-INET6
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Socket-INET6-%{version}.tar.gz
Patch0:         IO-Socket-INET6-2.72-fix_die_in_test.patch
Patch1:         IO-Socket-INET6-2.72-bz1207174-fix_random_test_error.patch
BuildArch:      noarch
%if %{with perl_IO_Socket_INET6_enables_optional_test}
%endif
Provides:       perl(IO::Socket::INET6)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Perl Object interface for AF_INET|AF_INET6 domain sockets.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-Socket-INET6-%{version}
%patch -P0 -p1
%patch -P1 -p1

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.73-12
- Prepare for Oreon 11 (RP1)
