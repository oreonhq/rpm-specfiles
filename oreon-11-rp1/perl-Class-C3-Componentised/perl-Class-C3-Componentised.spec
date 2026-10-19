%global source0_hash 3051b146dc1efeaea1a9a2e9e6b1773080995b898ab583f155658d5fc80b9693
Name:           perl-Class-C3-Componentised
Version:        1.001002
Release:        24%{?dist}
Summary:        Load mix-ins or components to your C3-based class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-C3-Componentised
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-C3-Componentised-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::C3) >= 0.20
Requires:       perl(Class::Inspector) >= 1.32
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::C3)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
