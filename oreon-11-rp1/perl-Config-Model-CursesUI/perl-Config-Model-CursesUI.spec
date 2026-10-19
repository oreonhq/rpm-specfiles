%global source0_hash ceba8e879c4cce41ad2b3dc8488413f37480aaeaa78b446e182ff0bce5dac981
Name:           perl-Config-Model-CursesUI
Version:        1.107
Release:        1%{?dist}
Summary:        Curses interface to edit config data
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Config-Model-CursesUI
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-CursesUI-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Model)
BuildRequires:  perl(Config::Model::Exception)
BuildRequires:  perl(Config::Model::ObjTreeScanner)
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(Curses::UI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This class provides a Curses::UI interface to configuration data managed by
Config::Model.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Model-CursesUI-%{version}

%build

/usr/bin/perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
