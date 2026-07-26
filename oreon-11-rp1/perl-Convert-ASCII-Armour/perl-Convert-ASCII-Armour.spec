%global source0_hash 97e8acb6eb2a2a91af7d6cf0d2dff6fa42aaf939fc7d6d1c6057a4f0df52c904

Name:           perl-Convert-ASCII-Armour
Version:        1.4
Release:        55%{?dist}
Summary:        Convert binary octets into ASCII armored messages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-ASCII-Armour
Source0:        https://cpan.metacpan.org/authors/id/V/VI/VIPUL/Convert-ASCII-Armour-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Data::Dumper)

%description
This module converts hashes of binary octets into ASCII messages
suitable for transfer over 6-bit clean transport channels.  The
encoded ASCII resembles PGP's armored messages, but are in no way
compatible with PGP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Convert-ASCII-Armour-%{version}

for file in lib/Convert/ASCII/*.pm ; do
  perl -pi -e '$_=undef if (/^\#\!/ and $.==1)' $file
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Shipping just ARTISTIC would be misleading
perldoc -t perlgpl > COPYING

%check
make test

%files
%license ARTISTIC COPYING
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
