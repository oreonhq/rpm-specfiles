%global source0_hash 2ec178da3b9899e4b466ab8b71edbb2bf23a0307ebe02fec7aa1f5826f61f55a

Name:           perl-File-Path-Tiny
Version:        1.0
Release:        14%{?dist}
Summary:        Recursive versions of mkdir() and rmdir() without as much overhead as File::Path
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Path-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMUEY/File-Path-Tiny-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
# Tests only
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

%description
The goal here is simply to provide recursive versions of mkdir() and
rmdir() with as little code and overhead as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Path-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
