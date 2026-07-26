%global source0_hash 46ec55c4b2c158fb9e3bd5c63aaa10695fee8508ef4ec958774dd8eaccab3847

Name:           perl-User-Identity
Version:        4.00
Release:        2%{?dist}
Summary:        Maintains info about a physical person
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/User-Identity
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/User-Identity-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Geography::Countries)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Report) >= 1.42
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
# Test Suite
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(warnings)
BuildRequires:  perl(Hash::Ordered)
# Dependencies
Requires:       perl(Geography::Countries)

%description
A module designed to store and maintain a set of informational objects that
are related to one user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n User-Identity-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ChangeLog README.md
%{perl_vendorlib}/Mail/
%{perl_vendorlib}/User/
%{_mandir}/man3/Mail::Identity.3*
%{_mandir}/man3/User::Identity.3*
%{_mandir}/man3/User::Identity::Archive.3*
%{_mandir}/man3/User::Identity::Archive::Plain.3*
%{_mandir}/man3/User::Identity::Collection.3*
%{_mandir}/man3/User::Identity::Collection::Emails.3*
%{_mandir}/man3/User::Identity::Collection::Locations.3*
%{_mandir}/man3/User::Identity::Collection::Systems.3*
%{_mandir}/man3/User::Identity::Collection::Users.3*
%{_mandir}/man3/User::Identity::Item.3*
%{_mandir}/man3/User::Identity::Location.3*
%{_mandir}/man3/User::Identity::System.3*

%changelog
%autochangelog
