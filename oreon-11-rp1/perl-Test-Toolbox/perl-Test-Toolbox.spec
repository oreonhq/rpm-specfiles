%global source0_hash 4020b5c7f3a15ac9b187d05dfd9816b8030ec0d4a47ff8373f7633bb614ebdc3
Name:           perl-Test-Toolbox
Version:        0.4
Release:        28%{?dist}
Summary:        Tools for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Toolbox
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Toolbox-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Basename)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
