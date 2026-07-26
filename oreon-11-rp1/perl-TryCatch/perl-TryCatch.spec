%global source0_hash ba88e73ded35d83caf0589d776cf8f91fad908df7fe7a4bd1274c6611336da9b

# Run optional tests
%{bcond_without perl_TryCatch_enables_optional_test}

Name:           perl-TryCatch
Version:        1.003002
Release:        41%{?dist}
Summary:        First class try catch semantics for Perl, without source filters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TryCatch
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASH/TryCatch-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# perl-podlators (pod2text) not used
BuildRequires:  perl(ExtUtils::Depends) >= 0.302
# File::Copy::Recursive not used
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install) >= 0.79
BuildRequires:  perl(Module::Install::Can)
BuildRequires:  perl(Module::Install::Metadata)
# Path::Class not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:  perl(B::Hooks::OP::PPAddr) >= 0.03
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Declare) >= 0.005007
BuildRequires:  perl(Devel::Declare::Context::Simple)
BuildRequires:  perl(Devel::PartialDump)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::clean) >= 0.20
BuildRequires:  perl(Parse::Method::Signatures) >= 1.003012
BuildRequires:  perl(Scope::Upper) >= 0.06
BuildRequires:  perl(Sub::Exporter) >= 0.979
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_TryCatch_enables_optional_test}
# Optional tests:
BuildRequires:  perl(MooseX::Types::Structured)
# XML::SAX::Base useless without XML::SAX::Expat
# XML::SAX::Expat not yet packaged
%endif
Requires:       perl(B::Hooks::EndOfScope) >= 0.12
Requires:       perl(B::Hooks::OP::PPAddr) >= 0.03
Requires:       perl(Devel::Declare) >= 0.005007
Requires:       perl(namespace::clean) >= 0.20
Requires:       perl(Parse::Method::Signatures) >= 1.003012
Requires:       perl(Scope::Upper) >= 0.06
Requires:       perl(Sub::Exporter) >= 0.979

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((B::Hooks::EndOfScope|B::Hooks::OP::PPAddr|Devel::Declare|namespace::clean|Parse::Method::Signatures|Scope::Upper|Sub::Exporter)\\)$

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

%check
make test

%files
%doc Changes README eg
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/TryCatch*
%{_mandir}/man3/*

%changelog
%autochangelog
