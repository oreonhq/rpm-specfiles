%global source0_hash 67b588e81d5f37301ff0f6c57d21fb6429cb2f826cc54e0fe897d360961b0fab
%bcond_without perl_Crypt_GCrypt_enables_optional_test
Name:           perl-Crypt-GCrypt
Version:        1.26
Release:        1%{?dist}
Summary:        Perl interface to libgcrypt library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-GCrypt
Source0:        https://cpan.metacpan.org/authors/id/A/AA/AAR/Crypt-GCrypt-%{version}.tar.gz
Patch0:         Crypt-GCrypt-1.26-libgcrypt_1_6_support.diff
Patch1:         Crypt-GCrypt-1.26-Correct-some-warnings.patch
Patch2:         Crypt-GCrypt-1.26-Use-an-encryption-key-in-the-test-suite.patch
Patch3:         perl-Crypt-GCrypt-c99.patch
%if %{with perl_Crypt_GCrypt_enables_optional_test}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Devel::Size)
BuildRequires:  perl(ExtUtils::Liblist)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Crypt::GCrypt provides a Perl interface to the libgcrypt cryptographic
functions. It currently supports symmetric ciphers such as AES/Rijndael,
Twofish, Triple DES, Arcfour etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-GCrypt-%{version}
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if !%{with perl_Crypt_GCrypt_enables_optional_test}
rm t/03-pod.t t/04-podcoverage.t t/05-size.t t/07-thread.t
perl -i -ne 'print $_ unless m{t/(?:03-pod|04-podcoverage|05-size|07-thread)\.t}' MANIFEST
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
