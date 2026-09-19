%global source0_hash 4020b5c7f3a15ac9b187d05dfd9816b8030ec0d4a47ff8373f7633bb614ebdc3

Name:           perl-Test-Toolbox
Version:        0.4
Release:        28%{?dist}
Summary:        Tools for testing
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Toolbox
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Toolbox-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Cwd)
BuildRequires:  perl-generators

Requires:       perl(File::Basename)

%description
Test::Toolbox provides tools for automated testing, much like other testing
modules, such as Test::More and Test::Simple. Test::Toolbox provides
a different flavor of tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Toolbox-%{version}

rm -f lib/Test/Toolbox.pod

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
