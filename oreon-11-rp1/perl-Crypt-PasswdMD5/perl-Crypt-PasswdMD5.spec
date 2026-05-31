%global source0_hash 42bf929345109585d4956902557ece35d061eda438e7894f86e7075741280759

%global cpan_version 1.43

Name:           perl-Crypt-PasswdMD5
# Keep 1-digit version because of history
Version:        %(echo '%{cpan_version}' | sed 's/\.\(.\)/.\1./')
Release:        1%{?dist}
Summary:        Provides interoperable MD5-based crypt() functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-PasswdMD5
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Crypt-PasswdMD5-1.43.tgz

Patch0:         Crypt-PasswdMD5-1.43-d:md5-version.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::MD5) >= 2.53
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 1.001002
# Dependencies:
# (none)

%description
This package provides MD5-based crypt() functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Crypt-PasswdMD5-%{cpan_version}

# Specify version requirement for Digest::MD5
# This avoids the need to add an explicit dependency in the spec file
# and the need to filter the underspecified auto-generated dependency
%patch -P0

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE-GPL-3
%doc AI_POLICY.md Changes README SECURITY.md
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::PasswdMD5.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.3-1
- Import
