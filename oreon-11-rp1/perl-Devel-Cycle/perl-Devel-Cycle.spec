%global source0_hash fd3365c4d898b2b2bddbb78a46d507a18cca8490a290199547dab7f1e7390bc2

Name:           perl-Devel-Cycle
Version:        1.12
Release:        33%{?dist}
Summary:        Find memory cycles in objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Cycle
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Cycle-%{version}.tar.gz
Patch0:         Devel-Cycle-1.11-512.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(PadWalker) >= 1.0
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(PadWalker) >= 1.0

Provides:       perl(Devel::Cycle)
%description
This is a simple developer's tool for finding circular references in
objects and other types of references. Because of Perl's reference-count
based memory management, circular references will cause memory leaks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-Cycle-%{version}

# Fix a Perl 5.12 incompatibility (#757274, CPAN RT#56681)
%patch -P 0 -p1

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
%{perl_vendorlib}/Devel/
%{_mandir}/man3/Devel::Cycle.3*

%changelog
%autochangelog
