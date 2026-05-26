Name:           perl-UNIVERSAL-require
Version:        0.19
Release:        14%{?dist}
Summary:        Require() modules from a variable
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UNIVERSAL-require
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/UNIVERSAL-require-0.19.tar.gz

Patch0:         UNIVERSAL-require-0.18-provides.patch
# oreon url source checksums begin
%global source0_sha256 d467cd26e06c8c3b203fd3bc0796ae6c837ac5e310093c82267ff5df850f1a03
%global source0_file UNIVERSAL-require-0.19.tar.gz
# oreon url source checksums end
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
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.47
# Dependencies
Requires:       perl(UNIVERSAL)

%description
%{summary}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/UNIVERSAL-require-0.19.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d467cd26e06c8c3b203fd3bc0796ae6c837ac5e310093c82267ff5df850f1a03" || { echo "oreon: Source0 SHA256 mismatch for UNIVERSAL-require-0.19.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n UNIVERSAL-require-%{version}

# Hide "package UNIVERSAL" from rpm to avoid bogus provide
%patch -P 0

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/UNIVERSAL::require.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19-14
- Prepare for Oreon 11 (RP1)
