%global source0_hash 74ac10bf66443ea813fb37d2ff5219c4d8e685379272d6699c812a39d91f3c1d
%bcond_without XSAccessor
Name:           perl-PPI
Version:        1.291
Release:        1%{?dist}
Summary:        Parse, Analyze and Manipulate Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPI
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/PPI-%{version}.tar.gz
BuildArch:      noarch
%if %{with XSAccessor}
%endif
Requires:       perl(Task::Weaken)
%global __provides_exclude ^perl\\(PPI::.+\\)$
Provides:       perl(PPI) = %{version}
Provides:       perl(PPI::Util) = %{version}
Provides:       perl(PPI::Dumper) = %{version}
Provides:       perl(PPI::Document) = %{version}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Object)
BuildRequires:  perl(Test::SubCalls)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Parse, analyze and manipulate Perl (without perl).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n PPI-%{version}

# Remove spurious executable bits
find . -type f -exec chmod -c -x {} \;

%if %{without XSAccessor}
rm lib/PPI/XSAccessor.pm
sed -i '/^lib\/PPI\/XSAccessor\.pm$/d' MANIFEST
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
