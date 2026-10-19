%global source0_hash 6622e1b5e5af952b1711aea247bdcb1b91c2aac0f11f32f819a2d07e11dd2845
Name:           perl-HTTP-Cache-Transparent
Version:        1.4
Release:        27%{?dist}
Summary:        Cache the result of http get-requests persistently
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Cache-Transparent
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTIASH/HTTP-Cache-Transparent-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
