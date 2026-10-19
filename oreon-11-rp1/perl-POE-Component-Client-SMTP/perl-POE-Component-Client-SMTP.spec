%global source0_hash 6d6961cc3f13554439c5abde345a840a546fce8453482ccf48f60d15e4a58a35
%bcond_without perl_POE_Component_Client_SMTP_enables_optional_test
Name:           perl-POE-Component-Client-SMTP
Version:        0.22
Release:        46%{?dist}
Summary:        Asynchronous mail sending with POE
License:        GPL-1.0-or-later OR Artistic-1.0-Perl        
URL:            https://metacpan.org/release/POE-Component-Client-SMTP
Source0:        https://cpan.metacpan.org/authors/id/U/UL/ULTRADM/POE-Component-Client-SMTP-%{version}.tar.gz
Patch0:         POE-Component-Client-SMTP-0.22-Normalize-shebangs.patch
BuildArch:      noarch
%if %{with perl_POE_Component_Client_SMTP_enables_optional_test}
%endif
Requires:       perl(POE) >= 0.31
Requires:       perl(POE::Filter::Transparent::SMTP) >= 0.2
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((POE|POE::Filter::Transparent::SMTP)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Filter::Transparent::SMTP)
BuildRequires:  perl(POE::Wheel::ListenAccept)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
POE::Component::Client::SMTP allows you to send email messages 
in an asynchronous manner, using POE.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Client-SMTP-%{version}
%patch -P0 -p1
chmod -x LICENSE README Changes COPYING TODO eg/*

%build

perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
