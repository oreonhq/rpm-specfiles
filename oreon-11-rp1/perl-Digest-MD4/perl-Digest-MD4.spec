%global source0_hash 665110bba32470f398f311cd6462fd8975d7c83675ff674bc2f6c7b72b0caaa6

Name:		perl-Digest-MD4
Version:	1.9
Release:	45%{?dist}
Summary:	Perl interface to the MD4 Algorithm
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Digest-MD4
Source0:	https://cpan.metacpan.org/modules/by-module/Digest/Digest-MD4-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Encode)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(MIME::Base64)
# Dependencies
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
The Digest::MD4 module allows you to use the RSA Data Security Inc. MD4 Message
Digest algorithm from within Perl programs. The algorithm takes as input a
message of arbitrary length and produces as output a 128-bit "fingerprint" or
"message digest" of the input.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Digest-MD4-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README rfc1320.txt
%{perl_vendorarch}/Digest/
%{perl_vendorarch}/auto/Digest/
%{_mandir}/man3/Digest::MD4.3*

%changelog
%autochangelog
