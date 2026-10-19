%global source0_hash ea93d97f6c0be0232f8b07ac0584dc3cd13e7a191dd03cca639ade02f44b3b69
%bcond_with core_iedoc
Name:           perl-Test-WWW-Selenium
Version:        1.36
Release:        1%{?dist}
Summary:        Perl Client for the Selenium Remote Control test tool
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Apache-2.0
URL:            https://metacpan.org/release/Test-WWW-Selenium
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTP/Test-WWW-Selenium-%{version}.tar.gz
BuildArch:      noarch
%if %with core_iedoc
%endif
Requires:       perl(Time::HiRes)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Mock::LWP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Selenium Remote Control (SRC) is a test tool that allows you to write
automated web application UI tests in any programming language against any
HTTP website using any mainstream JavaScript-enabled browser. SRC provides
a Selenium Server, which can automatically start/stop/control any supported
browser. It works by using Selenium Core, a pure-HTML+JS library that
performs automated tasks in JavaScript; the Selenium Server communicates
directly with the browser using AJAX (XmlHttpRequest).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-WWW-Selenium-%{version}

%if %with core_iedoc
# Newer API definition
mkdir -p target
unzip -qc %{_datadir}/java/selenium-core.jar core/iedoc.xml >target/iedoc.xml
%endif

%build

%if %with core_iedoc
%{__perl} util/create_www_selenium.pl
%endif
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
