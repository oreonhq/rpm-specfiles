%global source0_hash 35d5b03efc09f67f3a3155c9624126c3e162c8e3ca98ff826db358533a44c4bb

# Use optional Class::XSAccessor
%bcond_without perl_Class_Accessor_Grouped_enables_Class_XSAccessor
# Run optional test
%bcond_without perl_Class_Accessor_Grouped_enables_optional_test
# Support arbitrary method names using Sub::Name
%bcond_without perl_Class_Accessor_Grouped_enables_Sub_Name

Name:           perl-Class-Accessor-Grouped
Version:        0.10014
Release:        24%{?dist}
Summary:        Build groups of accessors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Accessor-Grouped
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-Accessor-Grouped-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::HasCompiler)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(mro)
BuildRequires:  perl(Scalar::Util)
# Optional run-time:
%if %{with perl_Class_Accessor_Grouped_enables_Sub_Name}
BuildRequires:  perl(Sub::Name) >= 0.05
%endif
%if %{with perl_Class_Accessor_Grouped_enables_Class_XSAccessor}
BuildRequires:  perl(Class::XSAccessor) >= 1.19
%endif
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
%if %{with perl_Class_Accessor_Grouped_enables_Sub_Name}
BuildRequires:  perl(Devel::Hide)
%endif
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
%if %{with perl_Class_Accessor_Grouped_enables_optional_test}
# Optional tests:
# MRO::Compat not used on Perl >= 5.9.5
BuildRequires:  perl(Package::Stash)
%endif
%if %{with perl_Class_Accessor_Grouped_enables_Class_XSAccessor}
Recommends:     perl(Class::XSAccessor) >= 1.19
%endif
Requires:       perl(mro)
%if %{with perl_Class_Accessor_Grouped_enables_Sub_Name}
Recommends:     perl(Sub::Name) >= 0.05
%endif

%{?perl_default_filter}

%description
This class lets you build groups of accessors that will call different
getters and setters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Accessor-Grouped-%{version}
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
