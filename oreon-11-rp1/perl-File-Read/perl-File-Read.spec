%global source0_hash 3c48225adb6b26c86398c92b00076fb620948f3eb834936adbb86f93f9c903b1

Name:           perl-File-Read
Version:        0.0801
Release:        45%{?dist}
Summary:        Unique interface for reading one or more files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Read
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAPER/File-Read-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Slurp)
# Tests only
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Text::Unidecode)

%description
This module mainly proposes functions for reading one or more files, with
different options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Read-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
