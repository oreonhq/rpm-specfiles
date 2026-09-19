%global source0_hash 128919127fca8787498f281292ced8da385750508803916b3686b64224b6c7a4

%global pkgname Async-MergePoint

Name:           perl-Async-MergePoint
Version:        0.04
Release:        36%{?dist}
Summary:        Resynchronize diverged control flow
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Async-MergePoint
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)

%description
Often in program logic, multiple different steps need to be taken that are
independent of each other, but their total result is needed before the next
step can be taken. In synchronous code, the usual approach is to do them
sequentially.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Async
%{_mandir}/man3/*

%changelog
%autochangelog
