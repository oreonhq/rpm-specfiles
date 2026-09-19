%global source0_hash e1a5bdde52505802664a9108a515c9e8e502cb7229a49de94f4081b1b2aeed84

Name:           perl-Class-Base
Version:        0.09
Release:        25%{?dist}
Summary:        Useful base class for deriving other modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Base
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Class-Base-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Clone)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(vars)

%description
This module implements a simple base class from which other modules can be
derived, thereby inheriting a number of useful methods such as new(),
init(), params(), clone(), error() and debug().

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Base-%{version}

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
%doc Changes CONTRIBUTORS README README.mkdn TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
