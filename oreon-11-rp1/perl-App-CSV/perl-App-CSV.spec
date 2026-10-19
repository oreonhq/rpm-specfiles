%global source0_hash f14c91135160fe8fe6d1e66a1ffffc0114e48765fb7480d93a30e10ab995c002
Name:           perl-App-CSV
Version:        0.08
Release:        1%{?dist}
Summary:        App::CSV Perl module
License:        MIT
URL:            https://metacpan.org/release/App-CSV
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAL/App-CSV-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(MooseX::Getopt)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::TempDir)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
App::CSV Perl module

%package -n csv
Summary: A CSV command line Tool
%description -n csv
A command-line tool to manipulate CSV (and other delimited, line-based) files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-CSV-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles csv usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n csv -f %{oreon_filedir}/csv.list

%changelog

%autochangelog
