%global source0_hash 46b4aec9a7d2c5749256d09dcf7ba4c2d00cddd41101482499ed88c766e9e8da

Name:           perl-ExtUtils-H2PM
Version:        0.11
Release:        9%{?dist}
Summary:        Automatically generate perl modules to wrap C header files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/ExtUtils-H2PM
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/ExtUtils-H2PM-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(List::Util) >= 1.39
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)

Requires:       perl(ExtUtils::CBuilder)

%{?perl_default_filter}

%description
This module assists in generating wrappers around system functionality,
such as socket() types or ioctl() calls, where the only interesting
features required are the values of some constants or layouts of structures
normally only known to the C header files. Rather than writing an entire XS
module just to contain some constants and pack/unpack functions, this
module allows the author to generate, at module build time, a pure perl
module containing constant declarations and structure utility functions.
The module then requires no XS module to be loaded at run time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-H2PM-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/ExtUtils
%{_mandir}/man3/ExtUtils::H2PM*

%changelog
%autochangelog
