%global source0_hash d0aabf4834c20ac411bea427c4a308b59a5fcaa327679ef5294c1d68ab71eed3

Summary:	Perl interface to the MD2 Algorithm
Name:		perl-Digest-MD2
Version:	2.04
Release:	39%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Url:		https://metacpan.org/release/Digest-MD2
Source0:	https://cpan.metacpan.org/authors/id/G/GA/GAAS/Digest-MD2-%{version}.tar.gz
Patch0:		Digest-MD2-2.03-utf8.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
# (no additional dependencies)
# Dependencies
# (no additional dependencies)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
The Digest::MD2 module allows you to use the RSA Data Security Inc. MD2 Message
Digest algorithm from within Perl programs. The algorithm takes as input a
message of arbitrary length and produces as output a 128-bit "fingerprint" or
"message digest" of the input.

The Digest::MD2 programming interface is identical to the interface of
Digest::MD5.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Digest-MD2-%{version}

# Convert docs to UTF-8 encoding
%patch -P 0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -a -empty -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%doc README Changes rfc1319.txt 
%{perl_vendorarch}/Digest/
%{perl_vendorarch}/auto/Digest/
%{_mandir}/man3/Digest::MD2.3*

%changelog
%autochangelog
