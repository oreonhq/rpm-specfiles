%global source0_hash 5cdfaeab32849d04a76b474ead81a5fd10a1128eb79e1620d81764f9bc13349f
%bcond_without perl_Test_POE_Client_TCP_enables_tls
Name:           perl-Test-POE-Client-TCP
Version:        1.26
Release:        22%{?dist}
Summary:        POE Component providing TCP client services for test cases
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-POE-Client-TCP
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Test-POE-Client-TCP-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(POE) >= 1.280
%if %{with perl_Test_POE_Client_TCP_enables_tls}
Recommends:     perl(POE::Component::SSLify)
%endif
Requires:       perl(POE::Filter::Line)
Requires:       perl(POE::Wheel::ReadWrite)
Requires:       perl(POE::Wheel::SocketFactory)
Requires:       perl(Socket) >= 2.013
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((POE|Socket)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Filter)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::POE::Client::TCP is a POE component that provides a TCP client
framework for inclusion in client component test cases, instead of having
to roll your own.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-POE-Client-TCP-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
