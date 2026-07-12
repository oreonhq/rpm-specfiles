%global source0_hash 91347d3a0b9a269180a3ea0e0d43f12c55dec3ddb974642f0e19093f907543d4

Name:		perl-Devel-OverloadInfo
Version:	0.008
Release:	2%{?dist}
Summary:	Introspect overloaded operators
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Devel-OverloadInfo
Source0:	https://cpan.metacpan.org/modules/by-module/Devel/Devel-OverloadInfo-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::HasCompiler) >= 0.023
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Text::ParseWords)
# Module Runtime
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(overload)
BuildRequires:	perl(Package::Stash) >= 0.14
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Util) >= 1.40
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(parent)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
Requires:	perl(Sub::Util) >= 1.40

Provides:       perl(Devel::OverloadInfo)
Provides:       perl(Devel::OverloadInfo)
%description
Devel::OverloadInfo returns information about overloaded operators for a
given class (or object), including where in the inheritance hierarchy the
overloads are declared and where the code implementing it is.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-OverloadInfo-%{version}

# Remove bundled ExtUtils::HasCompiler
rm -rf inc/
perl -ni -e 'print unless /^inc\//;' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Devel/
%{_mandir}/man3/Devel::OverloadInfo.3*

%changelog
%autochangelog
