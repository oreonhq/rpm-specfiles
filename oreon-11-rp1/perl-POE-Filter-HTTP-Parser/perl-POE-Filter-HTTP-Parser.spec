%global source0_hash e42d68ba3399ba9a54be5d61cf1296e44a1b9072352931a96cf03e8d947810af

Name:           perl-POE-Filter-HTTP-Parser
Version:        1.08
Release:        30%{?dist}
Summary:        HTTP POE filter for HTTP clients or servers
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Filter-HTTP-Parser
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Filter-HTTP-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
# bytes is strictly optional but needed for correctness
BuildRequires:  perl(bytes)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Parser) >= 0.06
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(POE::Filter)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(POE) >= 1.003
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(Test::More) >= 0.47
# Test::Pod not used
# Test::Pod::Coverage not used
BuildRequires:  perl(Test::POE::Client::TCP) >= 0.1
BuildRequires:  perl(Test::POE::Server::TCP) >= 0.16
Requires:       perl(HTTP::Parser) >= 0.06
# bytes is strictly optional but needed for correctess
Requires:       perl(bytes)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTTP::Parser\\)$

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

%check
make test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
