%global source0_hash 70c6c49d8b6c460746417a5098edd2a0fd31fd8b86c54bf8492e853c1f4e4b98
Name:           perl-Hash-Flatten
Version:        1.19
Release:        1%{?dist}
Summary:        Flatten/unflatten complex data hashes
License:        GPL-2.0-only
URL:            https://metacpan.org/release/Hash-Flatten
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBC/Hash-Flatten-%{version}.tar.gz
BuildArch:      noarch
Recommends:     perl(overload)
Provides:       perl(Hash::Flatten)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Log::Trace)
BuildRequires:  perl(Test::Assertions)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Converts back and forth between a nested hash structure and a flat hash of
delimited key-value pairs. Useful for protocols that only support key-value
pairs (such as CGI and DBMs).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Hash-Flatten-%{version}
iconv -f latin1 -t utf8 Changes > Changes.utf && \
    touch Changes.utf -r Changes && \
    mv Changes.utf Changes

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
