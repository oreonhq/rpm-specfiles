%global source0_hash 94509503ee74ea820183d070c11630ee5bc0fd8c12cb74fae953ed62e4a1ac17

Name:           perl-Apache-LogFormat-Compiler
Version:        0.36
Release:        19%{?dist}
Summary:        Compile a log format string to perl-code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Apache-LogFormat-Compiler
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Apache-LogFormat-Compiler-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-interpreter >= 0:5.008001
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(POSIX)
BuildRequires:  perl(POSIX::strftime::Compiler)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Try::Tiny) >= 0.12
BuildRequires:  perl(URI::Escape) >= 1.60
BuildRequires:  perl(warnings)

%description
Compile a log format string to perl-code. For faster generation of
access_log lines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-LogFormat-Compiler-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install

./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
