%global source0_hash ee5f20966ed15b17a705a12427324f8b8ee406b873d45d941fe98fcc08989493

Name:           perl-Config-Extend-MySQL
Version:        0.05
Release:        37%{?dist}
Summary:        Extend your favorite .INI parser module to read MySQL configuration file
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-Extend-MySQL
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAPER/Config-Extend-MySQL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(File::Read)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(UNIVERSAL::require)
Requires:       perl(Config::Tiny)

%{?perl_default_filter}

%description
This module extends other Config:: modules so they can read MySQL
configuration files. It works by slurping and preprocessing the files
before letting your favorite Config:: module parse the result.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Extend-MySQL-%{version}
# fix examples' shebang
sed -i -e '1s~#!.*~#!%{__perl}~' eg/*

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
