%global source0_hash 714f1a3e94f658029d108ca15ed20f0842e73559ae5fc1faee86d4f2195fcf8c

Name:           perl-Crypt-Blowfish_PP
Version:        1.12
Release:        40%{?dist}
Summary:        Blowfish encryption algorithm implemented purely in Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/pod/release/MATTBM/Crypt-Blowfish_PP-1.12/Blowfish_PP.pm
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTBM/Crypt-Blowfish_PP-1.12.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%{?perl_default_filter}

Provides:       perl(Crypt::Blowfish_PP)
Provides:       perl(Crypt::Blowfish_PP)
%description
The Crypt::Blowfish_PP module provides for users to use the Blowfish
encryption algorithm in perl. The implementation is entirely Object
Oriented, as there is quite a lot of context inherent in making blowfish
as fast as it is. The key is anywhere between 64 and 448 bits (8 and 56
bytes), and should be passed as a packed string. The transformation itself
is a 16-round Feistel Network, and operates on a 64 bit block.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Crypt-Blowfish_PP-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%check
make test


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%files
%doc README CHANGELOG
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
%autochangelog
