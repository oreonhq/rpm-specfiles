%global source0_hash 13b932dbb51a1b79560ff707d8b2d1489f65fa7bbebf080dee195c0e81b0c42e

Name:           perl-Encode-DoubleEncodedUTF8
Version:        0.05
Release:        35%{?dist}
Summary:        Fix double encoded UTF-8 bytes to the correct one
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Encode-DoubleEncodedUTF8
Source0:        https://cpan.metacpan.org/modules/by-module/Encode/Encode-DoubleEncodedUTF8-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Include)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::TestBase)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2.12
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(strict)
# Tests
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Encode::DoubleEncodedUTF8 adds a new encoding utf-8-de and fixes
double encoded utf-8 bytes found in the original bytes to the correct
Unicode entity.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Encode-DoubleEncodedUTF8-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
