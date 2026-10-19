%global source0_hash c91c96ca48e2ff799b2400ea165ccf87ef8dac62d7f2a48ccbda865e6d20d018
Name:           perl-Test-Module-Used
Version:        0.2.6
Release:        1%{?dist}
Summary:        Test required module is really used and vice versa between lib/t and META.yml
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Module-Used
Source0:        https://cpan.metacpan.org/authors/id/T/TS/TSUCCHI/Test-Module-Used-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(version) >= 0.77
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(version\\)$
# oreon:deps
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Used)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module reads META.yml and gets build_requires and requires. It compares
required module is really used and used module is really required.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Module-Used-%{version}
find -type f -exec chmod -x {} +

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
