%global source0_hash d13d8da7fdcd6d906054e4760fc28a718aec91bd3cf067a58927fb7cb1c09d6c
Name:           perl-CGI-Struct
Version:        1.21
Release:        33%{?dist}
Summary:        Build structures from CGI data
License:        LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/CGI-Struct
Source0:        https://cpan.metacpan.org/authors/id/F/FU/FULLERMD/CGI-Struct-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Deep::NoTest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
CGI::Struct lets you transform CGI data keys that look like perl data
structures into actual perl data structures.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Struct-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
