%global source0_hash 890178671cab1a7e44bb8754209127ac5f2d2b5b5d53ea399552cfcc2ab1ff19

Name:           perl-Test-Dist-VersionSync
Version:        1.2.0
Release:        27%{?dist}
Summary:        Verify that all the modules in a distribution have the same version number
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Test-Dist-VersionSync
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUBERTG/Test-Dist-VersionSync-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
The Test-Dist-VersionSync gives perl developers an easy way to verify that all
the modules in a distribution have the same version number.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Dist-VersionSync-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*

%changelog
%autochangelog
