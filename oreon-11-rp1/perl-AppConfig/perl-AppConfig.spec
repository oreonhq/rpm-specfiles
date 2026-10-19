%global source0_hash 1177027025ecb09ee64d9f9f255615c04db5e14f7536c344af632032eb887b0f
Name:           perl-AppConfig
Version:        1.71
Release:        1%{?dist}
Summary:        Perl module for reading configuration files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AppConfig
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/AppConfig-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(AppConfig)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
AppConfig has a powerful but easy to use module for parsing
configuration files.  It also has a simple and efficient module for
parsing command line arguments.  For fully-featured command line
parsing, a module is provided for interfacing AppConfig to Johan
Vromans' extensive Getopt::Long module.  Johan will continue to
develop the functionality of this package and its features will
automatically become available through AppConfig.

# filter out the unversioned provide AppConfig::State from Getopt.pm:
# RPM 4.8 style
%{?filter_setup:
%filter_from_provides /^perl(AppConfig::State)$/d
%?perl_default_filter
}
# RPM 4.9 style
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(AppConfig::State\\)$

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n AppConfig-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
chmod -R u+w $RPM_BUILD_ROOT
%oreon_autofiles main

%check

AUTOMATED_TESTING=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
