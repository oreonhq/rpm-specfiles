%global source0_hash bc9a4aa38ec98f0a98289e35abf9a17c2f2a3239a2209a329800e0970aa2e0c5

Name:           perl-Hash-Diff
Version:        0.010
Release:        22%{?dist}
Summary:        Return difference between two hashes as a hash
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Hash-Diff
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOLAV/Hash-Diff-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Test::use::ok)

%{?perl_default_filter}

%description
Hash::Diff returns the difference between two hashes as a hash.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-Diff-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README.md
%{perl_vendorlib}/Hash/Diff.pm
%{_mandir}/man3/Hash::Diff.3pm*

%changelog
%autochangelog
