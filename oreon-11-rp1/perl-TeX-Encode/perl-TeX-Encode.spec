%global source0_hash 3f58f908ee272b4438cf338646941cb7d5201e4ebf5e7bf335d70d6fbb7399cf

Name:		perl-TeX-Encode
Version:	2.010
Release:	13%{?dist}
Summary:	Encoding to LaTeX escapes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/TeX-Encode
Source0:	https://cpan.metacpan.org/authors/id/A/AT/ATHREEF/TeX-Encode-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(blib)
BuildRequires:	perl(Carp)
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:	perl(Encode)
BuildRequires:	perl(Encode::Encoding) >= 0.1
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Module::Metadata)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More) >= 0.1
BuildRequires:	perl(utf8)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)

%description
This module provides encoding to LaTeX escapes from utf8 using mapping tables
in Pod::LaTeX and HTML::Entities. This covers only a subset of the Unicode 
character table (undefined warnings will occur for non-mapped chars).

Mileage will vary when decoding (converting LaTeX to utf8), as LaTeX is in
essence a programming language, and this module does not implement LaTeX.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TeX-Encode-%{version}

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
%license LICENSE
%{perl_vendorlib}/TeX/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
