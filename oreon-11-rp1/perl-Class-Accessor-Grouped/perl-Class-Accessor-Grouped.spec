%global source0_hash 35d5b03efc09f67f3a3155c9624126c3e162c8e3ca98ff826db358533a44c4bb
%bcond_without perl_Class_Accessor_Grouped_enables_Class_XSAccessor
%bcond_without perl_Class_Accessor_Grouped_enables_optional_test
%bcond_without perl_Class_Accessor_Grouped_enables_Sub_Name
Name:           perl-Class-Accessor-Grouped
Version:        0.10014
Release:        24%{?dist}
Summary:        Build groups of accessors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Accessor-Grouped
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-Accessor-Grouped-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Class_Accessor_Grouped_enables_Sub_Name}
%endif
%if %{with perl_Class_Accessor_Grouped_enables_Class_XSAccessor}
%endif
%if %{with perl_Class_Accessor_Grouped_enables_Sub_Name}
%endif
%if %{with perl_Class_Accessor_Grouped_enables_optional_test}
%endif
%if %{with perl_Class_Accessor_Grouped_enables_Class_XSAccessor}
Recommends:     perl(Class::XSAccessor) >= 1.19
%endif
Requires:       perl(mro)
%if %{with perl_Class_Accessor_Grouped_enables_Sub_Name}
Recommends:     perl(Sub::Name) >= 0.05
%endif
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(ExtUtils::HasCompiler)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
