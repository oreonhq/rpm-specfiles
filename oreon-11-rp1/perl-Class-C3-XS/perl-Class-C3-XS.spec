%global source0_hash cf86d2575c1a374041d1ef3050cb36db6beda4e31295918aaeb2a029f0983afb

Name:		perl-Class-C3-XS
Version:	0.15
Release:	20%{?dist}
Summary:	XS speedups for Class::C3
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Class-C3-XS
Source0:	https://cpan.metacpan.org/modules/by-module/Class/Class-C3-XS-%{version}.tar.gz
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
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(Sub::Name)
# Dependencies
# (none)

# Avoid provides from private shared objects
%{?perl_default_filter}

%description
This contains XS performance enhancers for Class::C3 version 0.16 and
higher. The main Class::C3 package will use this package automatically if
it can find it. Do not use this package directly, use Class::C3 instead.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-C3-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorarch}/auto/Class/
%{perl_vendorarch}/Class/
%{_mandir}/man3/Class::C3::XS.3*

%changelog
%autochangelog
