%global source0_hash 39c53f6b3b02cbc73176564413b51d3c0f375f9760983fd579c27f558b169cfc
%bcond_without perl_Sub_Name_enables_optional_test
Name:		perl-Sub-Name
Version:	0.28
Release:        1%{?dist}
Summary:        Name - or rename - a sub
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Sub-Name
Source0:        https://www.cpan.org/modules/by-module/Sub/Sub-Name-%{version}.tar.gz
%if %{with perl_Sub_Name_enables_optional_test}
%endif
%{?perl_default_filter}
Provides:       perl(Sub::Name)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::CheckBin)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(feature)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module allows one to "name" or rename subroutines, including anonymous
ones.

Note that this is mainly for aid in debugging; you still cannot call the sub
by the new name (without some deep magic).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sub-Name-%{version}

%build

perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	optimize="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.28-5
- Prepare for Oreon 11 (RP1)
