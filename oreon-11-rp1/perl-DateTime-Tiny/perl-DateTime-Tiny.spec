%global source0_hash eaff931132fa8aa7a2e1688fd3d6d7ec55ea6eb071cacd4aaeb0cf91ce1af7d6

Name:           perl-DateTime-Tiny
Version:        1.08
Release:        3%{?dist}
Summary:        Date object, with as little code as possible
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/DateTime-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(overload)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(utf8)
Requires:       perl(Carp)
Requires:       perl(DateTime)

%description
DateTime::Tiny implements an extremely lightweight object that represents a
datetime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n DateTime-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README CONTRIBUTING.mkdn
%license LICENSE
%{perl_vendorlib}/DateTime*
%{_mandir}/man3/DateTime::Tiny*

%changelog
%autochangelog
