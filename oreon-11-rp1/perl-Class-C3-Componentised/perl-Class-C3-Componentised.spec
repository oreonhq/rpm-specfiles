%global source0_hash 3051b146dc1efeaea1a9a2e9e6b1773080995b898ab583f155658d5fc80b9693

Name:           perl-Class-C3-Componentised
Version:        1.001002
Release:        24%{?dist}
Summary:        Load mix-ins or components to your C3-based class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-C3-Componentised
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-C3-Componentised-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::C3) >= 0.20
BuildRequires:  perl(Class::Inspector) >= 1.32
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat) >= 0.09
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Class::C3) >= 0.20
Requires:       perl(Class::Inspector) >= 1.32

%{?perl_default_filter}

%description
This will inject base classes to your module using the Class::C3 method
resolution order.

Please note: these are not plugins that can take precedence over methods
declared in MyModule. If you want something like that, consider
MooseX::Object::Pluggable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-C3-Componentised-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
