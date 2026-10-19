%global source0_hash dcd89f76cba7a1c42c5aa5478e091799f335ed56dbe751585137495b8d7c7fbe
%bcond_with network_tests
Name:		perl-MetaCPAN-Client
Version:	2.040000
Release:        1%{?dist}
Summary:        A comprehensive, DWIM-featured client to the MetaCPAN API
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://github.com/CPAN-API/metacpan-client
Source0:        http://www.cpan.org/authors/id/M/MI/MICKEY/MetaCPAN-Client-%{version}.tar.gz
BuildArch:	noarch
%if %{with network_tests}
%endif
Requires:	perl(HTTP::Tiny) >= 0.056
Requires:	perl(IO::Socket::SSL) >= 1.42
Requires:	perl(Net::SSLeay) >= 1.49
%global __requires_exclude ^perl\\(HTTP::Tiny\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a hopefully-complete API-compliant interface to MetaCPAN
(https://metacpan.org/) with DWIM capabilities, to make your life easier.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MetaCPAN-Client-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

%if !%{with network_tests}
mv t/api/[a-z]*.t t/result_custom.t t/scroll.t ./
%endif
make test
%if !%{with network_tests}
mv ./result_custom.t ./scroll.t t/
mv ./[a-z]*.t t/api/
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
