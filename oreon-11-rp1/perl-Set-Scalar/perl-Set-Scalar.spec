%global source0_hash a3dc1526f3dde72d3c64ea00007b86ce608cdcd93567cf6e6e42dc10fdc4511d

Name:           perl-Set-Scalar
Version:        1.29
Release:        32%{?dist}
Summary:        Basic set operations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Set-Scalar
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Set-Scalar-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Carp)
# Dependencies
# (none)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Set-Scalar-%{version}

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
%doc ChangeLog README README.old
%{perl_vendorlib}/Set/
%{_mandir}/man3/Set::Scalar.3*
%{_mandir}/man3/Set::Scalar::Base.3*
%{_mandir}/man3/Set::Scalar::Null.3*
%{_mandir}/man3/Set::Scalar::Real.3*
%{_mandir}/man3/Set::Scalar::Universe.3*
%{_mandir}/man3/Set::Scalar::Valued.3*
%{_mandir}/man3/Set::Scalar::ValuedUniverse.3*
%{_mandir}/man3/Set::Scalar::Virtual.3*

%changelog
%autochangelog
