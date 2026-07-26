%global source0_hash 53aac3ea03978eb2d2c9141df3f6969fa60c7e6bd95c4928c34734aaa7efeabc

Name:           perl-Event-Lib
Version:        1.03
Release:        65%{?dist}
Summary:        Perl wrapper around libevent

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Event-Lib
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPARSEVAL/Event-Lib-%{version}.tar.gz
#https://rt.cpan.org/Public/Bug/Display.html?id=80644
Patch0:         https://rt.cpan.org/Ticket/Attachment/1136922/598341/lib-event.patch
# Restore compatibility with libevent 2.1, bug #1549504, CPAN RT#124603
Patch1:         Event-Lib-1.03-libevent_2_1.patch
# Adapt to changes in Perl 5.33.1, bug #1876460, CPAN RT#133340
Patch2:         Event-Lib-1.03-Fix-tests-on-indeed-non-blocking-UNIX-sockets.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Errno)
BuildRequires:  perl(GTop)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  libevent-devel >= 2.1

%description
This module is a Perl wrapper around libevent(3) as available from
http://monkey.org/~provos/libevent/.  It allows to execute a function
whenever a given event on a filehandle happens, a timeout occurs or a signal is
received.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Event-Lib-%{version}
%patch -P0 -p1 -b .orig
%patch -P1 -p1
%patch -P2 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
 INC=-I%{_includedir} LIBS="-L%{_libdir} -levent"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
#Known to fail - Upstream emailed
# t/20_signal.t
# t/51_cleanup_persistent.t
# t/90_leak.t
make test || :

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Event/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
