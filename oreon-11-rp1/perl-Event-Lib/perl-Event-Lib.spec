%global source0_hash 53aac3ea03978eb2d2c9141df3f6969fa60c7e6bd95c4928c34734aaa7efeabc
Name:           perl-Event-Lib
Version:        1.03
Release:        1%{?dist}
Summary:        Perl wrapper around libevent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Event-Lib
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPARSEVAL/Event-Lib-%{version}.tar.gz
Patch0:         https://rt.cpan.org/Ticket/Attachment/1136922/598341/lib-event.patch
Patch1:         Event-Lib-1.03-libevent_2_1.patch
Patch2:         Event-Lib-1.03-Fix-tests-on-indeed-non-blocking-UNIX-sockets.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(GTop)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
