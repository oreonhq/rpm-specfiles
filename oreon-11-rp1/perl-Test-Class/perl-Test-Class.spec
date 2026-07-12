%global source0_hash 40c1b1d388f0a8674769c27529f0cc3634ca0fd9d8f72b196c0531611934bc82

Name:           perl-Test-Class
Version:        0.52
Release:        14%{?dist}
Summary:        Easily create test classes in an xUnit/JUnit style
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Class
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Class-%{version}.tar.gz
Patch0:         perl-Test-Class-UTF8.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Attribute::Handlers) >= 0.77
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(MRO::Compat) >= 0.11
BuildRequires:  perl(Storable) >= 2.04
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder) >= 0.78
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::File) >= 1.09
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::Exception) >= 0.25
BuildRequires:  perl(Test::More) >= 1.001002
# Optional tests:
BuildRequires:  perl(Contextual::Return)
Requires:       perl(Attribute::Handlers) >= 0.77
Requires:       perl(MRO::Compat) >= 0.11
Requires:       perl(Storable) >= 2.04
Requires:       perl(Test::Builder) >= 0.78

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Attribute::Handlers|MRO::Compat|Storable|Test::Builder)\\)$

Provides:       perl(Test::Class)
Provides:       perl(Test::Class::Load)
%description
Test::Class provides a simple way of creating classes and objects to test
your code in an xUnit style.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Class-%{version}

# Fix up broken permissions
find -type f -exec chmod -c -x {} \;

# Fix character encoding in documentation
%patch -P0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Class.3*
%{_mandir}/man3/Test::Class::Load.3*
%{_mandir}/man3/Test::Class::MethodInfo.3*

%changelog
%autochangelog
