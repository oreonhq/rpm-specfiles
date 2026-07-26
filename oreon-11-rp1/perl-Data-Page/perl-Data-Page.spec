%global source0_hash 2efa52167d1f7ab35902cf32ae02776a623705d7919d4118981287b044ce3d8b

Name:           perl-Data-Page
Version:        2.03
Release:        20%{?dist}
Summary:        Help when paging through sets of results
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Page
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Data-Page-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(integer)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Page-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms}  $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENCE
%doc README Changes
%{perl_vendorlib}/Data
%{_mandir}/man3/*.3*

%changelog
%autochangelog
