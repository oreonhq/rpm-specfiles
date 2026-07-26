%global source0_hash 43be65d079156d708bdfb6e0436a20593e6a040125187e577262c85b353f73b7

Name:           perl-IO-Event
Version:        0.813
Release:        35%{?dist}
Summary:        Tied filehandles for nonblocking IO with object callbacks
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Event
Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/IO-Event-%{version}.tar.gz
# Fix a race in t/foked2.t test, bug #1105023, CPAN RT#92200
Patch0:         IO-Event-0.813-Fix-undeterministic-test-failures-in-t-forked2.t.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Impl::Perl)
BuildRequires:  perl(Carp)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(Event)
BuildRequires:  perl(Event::Watcher)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
Requires:       perl(AnyEvent)
Requires:       perl(IO::Socket::INET)
Requires:       perl(IO::Socket::UNIX)

%{?perl_default_filter}

%description
IO::Event provides a object-based callback system for handling nonblocking
IO. The design goal is to provide a system that just does the right thing
w/o the user needing to think about it much.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Event-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find %{buildroot} -type f -name .packlist -exec rm -f {} +

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
