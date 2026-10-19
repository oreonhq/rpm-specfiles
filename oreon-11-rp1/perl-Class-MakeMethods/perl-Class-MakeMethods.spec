%global source0_hash acac742e79d0ec8a7be4d8fb813a85ea44d47d19c0170cddb30644602b582c66
%global cpan_version 1.01
Name:           perl-Class-MakeMethods
Version:        %{cpan_version}0
Release:        1%{?dist}
Summary:        Generate common types of methods
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-MakeMethods
Source0:        https://cpan.metacpan.org/authors/id/E/EV/EVO/Class-MakeMethods-%{cpan_version}.tar.gz
Patch0:         Class-MakeMethods-1.009-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Class::MakeMethods framework allows Perl class developers to quickly
define common types of methods. When a module uses Class::MakeMethods or one
of its subclasses, it can select from a variety of supported method types, and
specify a name for each method desired. The methods are dynamically generated
and installed in the calling package.

Construction of the individual methods is handled by subclasses. This
delegation approach allows for a wide variety of method-generation techniques
to be supported, each by a different subclass. Subclasses can also be added to
provide support for new types of methods.

Over a dozen subclasses are available, including implementations of a variety
of different method-generation techniques. Each subclass generates several
types of methods, with some supporting their own open-eneded extension syntax,
for hundreds of possible combinations of method types.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-MakeMethods-%{cpan_version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
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
