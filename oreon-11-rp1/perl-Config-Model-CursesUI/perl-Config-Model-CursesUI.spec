%global source0_hash ceba8e879c4cce41ad2b3dc8488413f37480aaeaa78b446e182ff0bce5dac981

Name:           perl-Config-Model-CursesUI
Version:        1.107
Release:        16%{?dist}
Summary:        Curses interface to edit config data
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Config-Model-CursesUI
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-CursesUI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Model) >= 0.637
BuildRequires:  perl(Config::Model::Exception)
BuildRequires:  perl(Config::Model::ObjTreeScanner)
BuildRequires:  perl(Config::Model::Tester::Setup) >= 3.006
BuildRequires:  perl(Curses::UI) >= 0.9606
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

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

%check
./Build test

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
