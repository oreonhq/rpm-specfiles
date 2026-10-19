%global source0_hash e42d68ba3399ba9a54be5d61cf1296e44a1b9072352931a96cf03e8d947810af
Name:           perl-POE-Filter-HTTP-Parser
Version:        1.08
Release:        1%{?dist}
Summary:        HTTP POE filter for HTTP clients or servers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Filter-HTTP-Parser
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Filter-HTTP-Parser-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(HTTP::Parser) >= 0.06
Requires:       perl(bytes)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTTP::Parser\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Parser)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Filter)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::POE::Client::TCP)
BuildRequires:  perl(Test::POE::Server::TCP)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
POE::Filter::HTTP::Parser is a POE::Filter for HTTP which is based on
HTTP::Parser.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Filter-HTTP-Parser-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
