%global source0_hash 5881555d6187972a2382aa0d4db2d74c970b06774c621b6ca523739236d2d501
Name:           perl-Crypt-Twofish
Version:        2.18
Release:        1%{?dist}
Summary:        Twofish Encryption Algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-Twofish
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMS/Crypt-Twofish-%{version}.tar.gz
Patch0:         perl-Crypt-Twofish-makefile-c99.patch
Requires:       perl(Crypt::CBC)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Twofish is a 128-bit symmetric block cipher with a variable length (128,
192, or 256-bit) key, developed by Counterpane Labs. It is unpatented and
free for all uses, as described at http://www.counterpane.com/twofish.html.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Crypt-Twofish-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
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
