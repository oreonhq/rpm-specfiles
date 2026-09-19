%global source0_hash 74ac10bf66443ea813fb37d2ff5219c4d8e685379272d6699c812a39d91f3c1d

# PPI::XSAccessor is experimental
%if 0%{?rhel:1}
%bcond_with XSAccessor
%else
%bcond_without XSAccessor
%endif

Name:           perl-PPI
Version:        1.291
Release:        1%{?dist}
Summary:        Parse, Analyze and Manipulate Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPI
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/PPI-%{version}.tar.gz
BuildArch:      noarch
# =============== Module Build ======================
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) > 6.75
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# =============== Module Runtime ====================
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone) >= 0.30
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::MD5) >= 2.35
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable) >= 2.17
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(YAML::PP)
# =============== Optional Functionality ============
%if %{with XSAccessor}
BuildRequires:  perl(Class::XSAccessor)
%endif
# =============== Test Suite ========================
BuildRequires:  perl(B)
BuildRequires:  perl(Class::Inspector) >= 1.22
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Object) >= 0.07
BuildRequires:  perl(Test::SubCalls) >= 1.07
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)
# =============== Dependencies ======================
# Run-require Task::Weaken, see Changes for more details.
Requires:       perl(Task::Weaken)

# Filter out redundant unversioned provides
%global __provides_exclude ^perl\\(PPI::.+\\)$

Provides:       perl(PPI) = %{version}
Provides:       perl(PPI::Util) = %{version}
Provides:       perl(PPI::Dumper) = %{version}
Provides:       perl(PPI::Document) = %{version}
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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/PPI/
%{perl_vendorlib}/PPI.pm
%{_mandir}/man3/PPI*.3*

%changelog
%autochangelog
