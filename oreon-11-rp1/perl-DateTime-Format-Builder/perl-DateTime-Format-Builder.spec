%global source0_hash 61ffb23d85b3ca1786b2da3289e99b57e0625fe0e49db02a6dc0cb62c689e2f2
%bcond_without perl_DateTime_Format_Builder_enable_optional_tests
%global real_version   0.83
Name:           perl-DateTime-Format-Builder
Version:        0.8300
Release:        1%{?dist}
Summary:        Create DateTime parser classes and objects
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/DateTime-Format-Builder            
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Builder-0.83.tar.gz
BuildArch:      noarch
%if %{with perl_DateTime_Format_Builder_enable_optional_tests}
%endif
Provides:       perl(DateTime::Format::Builder) = %{version}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::HTTP)
BuildRequires:  perl(DateTime::Format::IBeat)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
DateTime::Format::Builder creates DateTime parsers. Many string formats of
dates and times are simple and just require a basic regular expression to
extract the relevant information. Builder provides a simple way to do this
without writing reams of structural code.

Builder provides a number of methods, most of which you'll never need, or at
least rarely need. They're provided more for exposing of the module's innards
to any sub-classes, or for when you need to do something slightly beyond what
is expected.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Format-Builder-%{real_version}

# POD doesn't like E<copy> very much...
perl -pi -e 's/E<copy>/(C)/' `find lib/ -type f`

# Silence rpmlint
sed -i '1s~^#!.*perl~#!%{__perl}~' t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8300-17
- Prepare for Oreon 11 (RP1)
