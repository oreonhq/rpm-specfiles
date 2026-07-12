%global source0_hash 4821a2de10ac7108f4dcb284a71b876981b0cb1ea6c5ed6afb177bf2e7cb8d73

Name:		perl-Data-Binary
Version:	0.01
Release:	21%{?dist}
Summary:	Simple detection of binary versus text in strings
License:	Artistic-2.0
URL:		https://metacpan.org/release/Data-Binary
Source0:	https://cpan.metacpan.org/modules/by-module/Data/Data-Binary-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
# (none)

Provides:       perl(Data::Binary)
%description
This simple module provides string equivalents to the -T / -B operators. Since
these only work on file names and file handles, this module provides the same
functions but on strings.

Note that the actual implementation is currently different, basically because
the -T / -B functions are in C/XS, and this module is written in pure Perl. For
now, anyway.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Binary-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc changes.txt README readme.txt
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::Binary.3*

%changelog
%autochangelog
