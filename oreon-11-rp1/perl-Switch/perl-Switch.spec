Name:		perl-Switch
Version:	2.17
Release:	35%{?dist}
Summary:	A switch statement for Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Switch
Source0:	https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/Switch-%{version}.tar.gz
Patch0:		Switch-2.17-Filter-1.50.patch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Carp)
BuildRequires:	perl(deprecate)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Filter::Util::Call)
BuildRequires:	perl(if)
BuildRequires:	perl(overload)
BuildRequires:	perl(strict)
BuildRequires:	perl(Text::Balanced)
BuildRequires:	perl(vars)
Requires:	perl(deprecate)
BuildArch:	noarch

%description
Switch.pm provides the syntax and semantics for an explicit case mechanism for 
Perl. The syntax is minimal, introducing only the keywords C<switch> and 
C<case> and conforming to the general pattern of existing Perl control 
structures. The semantics are particularly rich, allowing any one (or more) of 
nearly 30 forms of matching to be used when comparing a switch value with its 
various cases.

%prep
%setup -q -n Switch-%{version}
%patch -P0 -p1 -b .fixme

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Switch.pm
%{_mandir}/man3/*.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17-35
- Import
