%global source0_hash df890e6fb7686242569a8c71ad8f1a0140402230971d495bbfc44deb06519b3c

Name:           perl-XML-Parser-Lite-Tree
Version:        0.14
Release:        40%{?dist}
Summary:        Lightweight XML tree builder
License:        Artistic-2.0
URL:            https://metacpan.org/release/XML-Parser-Lite-Tree
Source0:        https://cpan.metacpan.org/authors/id/I/IA/IAMCAL/XML-Parser-Lite-Tree-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)

%description
This is a singleton class for parsing XML into a tree structure. How does
this differ from other XML tree generators? By using XML::Parser::Lite,
which is a pure perl XML parser. Using this module you can tree-ify simple
XML without having to compile any C.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Parser-Lite-Tree-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
