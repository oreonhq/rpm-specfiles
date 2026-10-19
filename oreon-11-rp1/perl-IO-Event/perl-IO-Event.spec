%global source0_hash 43be65d079156d708bdfb6e0436a20593e6a040125187e577262c85b353f73b7
Name:           perl-IO-Event
Version:        0.813
Release:        1%{?dist}
Summary:        Tied filehandles for nonblocking IO with object callbacks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Event
Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/IO-Event-%{version}.tar.gz
Patch0:         IO-Event-0.813-Fix-undeterministic-test-failures-in-t-forked2.t.patch
BuildArch:      noarch
Requires:       perl(AnyEvent)
Requires:       perl(IO::Socket::INET)
Requires:       perl(IO::Socket::UNIX)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Impl::Perl)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Event)
BuildRequires:  perl(Event::Watcher)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
