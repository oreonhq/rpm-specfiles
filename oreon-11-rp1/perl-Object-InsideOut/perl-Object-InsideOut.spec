%global source0_hash 9dfd6ca2822724347e0eb6759d00709425814703ad5c66bdb6214579868bcac4

Name:           perl-Object-InsideOut
Version:        4.05
Release:        31%{?dist}
Summary:        Comprehensive inside-out object support module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-InsideOut
Source0:        https://cpan.metacpan.org/modules/by-module/Object/Object-InsideOut-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(attributes)
BuildRequires:  perl(B)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper) >= 2.131
BuildRequires:  perl(Exception::Class) >= 1.32
BuildRequires:  perl(Scalar::Util) >= 1.23
# Optional run-time
%if %{undefined perl_bootstrap}
BuildRequires:  perl(Math::Random::MT::Auto) >= 6.18
%endif
BuildRequires:  perl(Want) >= 0.21
# Test only
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(threads)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(threads::shared)
# Optional tests
BuildRequires:  perl(Storable)
# Dependencies
Requires:       perl(Data::Dumper) >= 2.131
Requires:       perl(Scalar::Util) >= 1.23

# Remove underspecified dependencies
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Object::InsideOut\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Scalar::Util\\)

%if %{defined perl_bootstrap}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Math::Random::MT::Auto\\)
%endif

%description
This module provides comprehensive support for implementing classes using the
inside-out object model.

This module implements inside-out objects as anonymous scalar references that
are blessed into a class with the scalar containing the ID for the object
(usually a sequence number). Object data (i.e., fields) are stored within the
class's package in either arrays indexed by the object's ID, or hashes keyed
to the object's ID.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-InsideOut-%{version}

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
%doc examples/ Changes README
%{perl_vendorlib}/Bundle/
%{perl_vendorlib}/Object/
%{_mandir}/man3/Bundle::Object::InsideOut.3*
%{_mandir}/man3/Object::InsideOut.3*
%{_mandir}/man3/Object::InsideOut::Metadata.3*

%changelog
%autochangelog
