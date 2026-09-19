%global source0_hash 06d8d50e8cd3692a11cb4fb44a2f84e5476a98f0e2e6a4a0dfce9f67e55ddb53

Name:           perl-LWP-UserAgent-Determined
Version:        1.07
Release:        34%{?dist}
Summary:        Virtual browser that retries errors
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/LWP-UserAgent-Determined
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/LWP-UserAgent-Determined-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(LWP::UserAgent)
# Tests:
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP)
BuildRequires:  perl(Test)

%{?perl_default_filter}

%description
This class works just like LWP::UserAgent (and is based on it, by being a
subclass of it), except that when you use it to get a web page but run into
a possibly-temporary error (like a DNS lookup timeout), it'll wait a few
seconds and retry a few times.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LWP-UserAgent-Determined-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
