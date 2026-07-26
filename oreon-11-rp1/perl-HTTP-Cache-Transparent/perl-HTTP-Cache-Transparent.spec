%global source0_hash 6622e1b5e5af952b1711aea247bdcb1b91c2aac0f11f32f819a2d07e11dd2845

Name:           perl-HTTP-Cache-Transparent
Version:        1.4
Release:        27%{?dist}
Summary:        Cache the result of http get-requests persistently

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Cache-Transparent
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTIASH/HTTP-Cache-Transparent-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(LWP::UserAgent)

%{?perl_default_filter}

%description
HTTP::Cache::Transparent is an implementation of http get that keeps a
local cache of fetched pages to avoid fetching the same data from the
server if it hasn't been updated. The cache is stored on disk and is
thus persistent between invocations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Cache-Transparent-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README.md Changes
%{perl_vendorlib}/HTTP/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
