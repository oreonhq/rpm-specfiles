%global source0_hash 6210219264fc30534191959dbe0a64bf55b5a60c4ffec0d996769faa8335c9b7

%global cpan_version 1.202830

Name:           perl-WebService-Rajce
# Normalize version to dotted format
Version:        %(echo '%{cpan_version}' | sed 's/\(\....\)\(.\)/\1.\2/')
Release:        16%{?dist}
Summary:        Perl interface for www.rajce.idnes.cz
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-Rajce
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEK/WebService-Rajce-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time (No tests exhibiting the code are performed)
# AutoLoader not used at tests
# Carp not used at tests
# Digest::MD5 not used at tests
# Encode not used at tests
# Exporter not used at tests
# File::Basename not used at tests
# File::Path not used at tests
# Getopt::Long not used at tests
# Image::Magick not used at tests
# https URLs are passed to the LWP
# LWP::Protocol::https not used at tests
# Net::Netrc not used at tests
# Pod::Usage not used at tests
# POSIX not used at tests
# vars not used at tests
# WWW::Mechanize not used at tests
# XML::FeedPP not used at tests
# XML::Simple not used at tests
# Tests:
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More)
# Test::Pod::Coverage 1.08 not used
Requires:       perl(AutoLoader)
# https URLs are passed to the LWP
Requires:       perl(LWP::Protocol::https)

%description
This is a Perl library implementing an API of a photo gallery service running
on www.rajce.idnes.cz server.

%package tools
Summary:        Utilities for accessing www.rajce.idnes.cz
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch

%description tools
Command line tools for uploading and downloading images from a photo gallery
service running on www.rajce.idnes.cz server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WebService-Rajce-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
