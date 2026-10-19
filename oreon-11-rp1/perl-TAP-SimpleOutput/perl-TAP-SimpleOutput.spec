%global source0_hash 7899b42253e6be0ec70a633af05d5b1e387d30979cf1358bb405fe665f02cf89
Name:           perl-TAP-SimpleOutput
Version:        0.009
Release:        27%{?dist}
Summary:        Simple closure-driven TAP generator
License:        LicenseRef-Callaway-LGPLv2
URL:            https://metacpan.org/release/TAP-SimpleOutput
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/TAP-SimpleOutput-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Perl::Version)
Requires:       perl(Test::More) >= 0.98
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Perl::Version)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
We provide one function, counters(), that returns a number of simple closures
designed to help output TAP easily and correctly, with a minimum of fuss.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TAP-SimpleOutput-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
