%global source0_hash e4275e50931c94aff00436d7d0f2f990e29bc070f905a76e1c4b40810ddeab6f

Name:           perl-MooseX-Deprecated
Version:        0.005
Release:        20%{?dist}
Summary:        Mark attributes and methods as deprecated
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Deprecated
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/MooseX-Deprecated-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.3
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Callsite) >= 0.08
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose) >= 2.0600
BuildRequires:  perl(MooseX::Role::Parameterized) >= 1.00
BuildRequires:  perl(Test::Fatal) >= 0.007
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.005
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
MooseX::Deprecated is a parameterizable role that makes it easy to
deprecate particular attributes and methods in a class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Deprecated-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
