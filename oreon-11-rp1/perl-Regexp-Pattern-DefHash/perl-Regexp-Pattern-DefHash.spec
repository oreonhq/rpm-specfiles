%global source0_hash 9865d6289e0e49816926e3da6a168c41a1e6ee51004fe696cd08588d2285679c

Name:           perl-Regexp-Pattern-DefHash
Version:        0.001
Release:        13%{?dist}
Summary:        Regexp patterns related to DefHash
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Regexp-Pattern-DefHash
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Regexp-Pattern-DefHash-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(warnings)

%description
Regexp::Pattern::License provides a hash of regular expression patterns related
to legal software licenses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Regexp-Pattern-DefHash-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/Regexp::Pattern::DefHash*.*

%changelog
%autochangelog
