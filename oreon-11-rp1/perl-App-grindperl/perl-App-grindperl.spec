%global source0_hash d26b1f68777083451dc847c8b1d7e851d9511054590318033cea40a3cae06b0f
Name:           perl-App-grindperl
Version:        0.004
Release:        30%{?dist}
Summary:        Command-line tool to help build and test blead perl
License:        Apache-2.0
URL:            https://metacpan.org/release/App-grindperl
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/App-grindperl-%{version}.tar.gz
BuildArch:      noarch
Requires:       git
Requires:       make
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Hacking on the Perl source tree requires one to regularly build and test. The
grindperl tool helps automate some common configuration, build and test tasks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-grindperl-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
