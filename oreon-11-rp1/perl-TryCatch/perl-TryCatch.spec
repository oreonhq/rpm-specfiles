%global source0_hash ba88e73ded35d83caf0589d776cf8f91fad908df7fe7a4bd1274c6611336da9b
%{bcond_without perl_TryCatch_enables_optional_test}
Name:           perl-TryCatch
Version:        1.003002
Release:        41%{?dist}
Summary:        First class try catch semantics for Perl, without source filters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TryCatch
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASH/TryCatch-%{version}.tar.gz
%if %{with perl_TryCatch_enables_optional_test}
%endif
Requires:       perl(B::Hooks::EndOfScope) >= 0.12
Requires:       perl(B::Hooks::OP::PPAddr) >= 0.03
Requires:       perl(Devel::Declare) >= 0.005007
Requires:       perl(namespace::clean) >= 0.20
Requires:       perl(Parse::Method::Signatures) >= 1.003012
Requires:       perl(Scope::Upper) >= 0.06
Requires:       perl(Sub::Exporter) >= 0.979
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((B::Hooks::EndOfScope|B::Hooks::OP::PPAddr|Devel::Declare|namespace::clean|Parse::Method::Signatures|Scope::Upper|Sub::Exporter)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(B::Hooks::OP::PPAddr)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Declare)
BuildRequires:  perl(Devel::Declare::Context::Simple)
BuildRequires:  perl(Devel::PartialDump)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Install::Can)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(Parse::Method::Signatures)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Upper)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module aims to provide a nicer syntax and method to catch errors in
Perl, similar to what is found in other languages (such as Java, Python or
C++). The standard method of using eval {}; if ($@) {} is often prone to
subtle bugs, primarily that its far too easy to stomp on the error in error
handlers. And also eval/if isn't the nicest idiom.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TryCatch-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
