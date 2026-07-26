%global source0_hash 59f261815f7c7eb160053a96715e96d68569e4e4f3b05453e7c24d58bd458c96

Name:           perl-App-Cache
Summary:        Easy application-level caching
Version:        0.37
Release:        45%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/L/LB/LBROCARD/App-Cache-%{version}.tar.gz 
URL:            https://metacpan.org/release/App-Cache

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(warnings)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
The App::Cache module lets an application cache data locally. There are a
few times an application would need to cache data: when it is retrieving
information from the network or when it has to complete a large calculation.
For example, the Parse::BACKPAN::Packages module downloads a file off the
net and parses it, creating a data structure. Only then can it actually
provide any useful information for the programmer. Parse::BACKPAN::Packages
uses App::Cache to cache both the file download and data structures,
providing much faster use when the data is cached. This module stores data
in the home directory of the user, in a dot directory. For example, the
Parse::BACKPAN::Packages cache is actually stored underneath
"~/.parse_backpan_packages/cache/". This is so that permissions are not a
problem -- it is a per-user, per-application cache.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-Cache-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
