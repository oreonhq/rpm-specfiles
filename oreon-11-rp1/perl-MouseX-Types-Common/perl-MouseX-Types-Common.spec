%global source0_hash f8346f684571fd5897dd2a294aecfc6e72fa4f1ee64aef46371f5937d6998e6c

Name:           perl-MouseX-Types-Common
Version:        0.001000
Release:        12%{?dist}
Summary:        Set of commonly-used type constraints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://metacpan.org/dist/MouseX-Types-Common/
Source0:        http://cpan.metacpan.org/authors/id/G/GF/GFUJI/MouseX-Types-Common-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__chmod}
BuildRequires:  %{__make}
BuildRequires:  %{__sed}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators

BuildRequires:  perl(:VERSION) >= 5.6.2
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Mouse) >= 0.42
BuildRequires:  perl(MouseX::Types) >= 0.01
BuildRequires:  perl(MouseX::Types::Mouse)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(Test::Exception)

BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)


Provides:       perl(MouseX::Types::Common)
%description
A set of commonly-used type constraints that do not ship with Mouse
by default.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MouseX-Types-Common-%{version}
# Remove bundled modules
rm -r inc
%{__sed} -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
