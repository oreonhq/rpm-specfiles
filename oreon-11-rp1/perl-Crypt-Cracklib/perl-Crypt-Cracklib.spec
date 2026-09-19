%global source0_hash cf864ddffaec6b4697bd4e53030f320166c69c3b3aebf79ce25b9af30228567f

Name:           perl-Crypt-Cracklib
Version:        1.7
Release:        49%{?dist}
Summary:        Crypt-Cracklib - Perl interface to Alec Muffett's Cracklib
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-Cracklib
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-Cracklib-%{version}.tar.gz
Patch0:         Crypt-Cracklib-1.7-Fix-building-on-Perl-without-dot-in-INC.patch
Patch1:         Crypt-Cracklib-1.7-Detect-gzipped-dictionary.patch
# Build:
BuildRequires:  coreutils
BuildRequires:  cracklib-devel
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  cracklib-dicts
BuildRequires:  perl(Test::More)
# Optional Tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# Dependencies:
# (none)

%description
This module providers interaction with the system cracklib libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-Cracklib-%{version}

# Fix building on Perl without '.' in @INC
# https://github.com/dsully/perl-crypt-cracklib/issues/4
%patch -P0

# Detect gzipped dictionary
# https://github.com/dsully/perl-crypt-cracklib/issues/1
%patch -P1 -p1

# Unbundle bundled modules
rm -rf inc/

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps < /dev/null
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -name Cracklib.bs -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/Crypt::Cracklib.3*

%changelog
%autochangelog
