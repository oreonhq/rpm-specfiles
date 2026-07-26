%global source0_hash 71e327f1f6df862918c0a9db98d7760fcfa2d91a536779932a47d3534617c6fa

Name:           perl-Net-IP-CMatch
Version:        0.02
Release:        61%{?dist}
Summary:        Efficiently match IP addresses against IP ranges with C

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IP-CMatch
Source0:        https://cpan.metacpan.org/authors/id/B/BE/BEAU/Net-IP-CMatch-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)

%description
Net::IP::CMatch is based upon, and does the same thing as Net::IP::Match. The
unconditionally exported subroutine 'match_ip' determines if the IP to match
(first argument) matches any of the subsequent IP arguments. Match arguments
may be absolute quads, as '127.0.0.1', or contain mask bits as
'111.245.76.248/29'. A true return value indicates a match. It was written in
C, rather than a macro, preprocessed through perl's source filter mechanism
(as is Net::IP::Match), so that the IP arguments could be traditional perl
scalars. The C code is lean and mean (IMHO).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IP-CMatch-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/Net/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
