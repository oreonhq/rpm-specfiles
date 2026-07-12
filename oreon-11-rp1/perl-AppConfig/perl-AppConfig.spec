%global source0_hash 1177027025ecb09ee64d9f9f255615c04db5e14f7536c344af632032eb887b0f

Name:           perl-AppConfig
Version:        1.71
Release:        34%{?dist}
Summary:        Perl module for reading configuration files

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AppConfig
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/AppConfig-%{version}.tar.gz

BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl%{?fedora:-interpreter}
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime:
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long) >= 2.17
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# Optional Tests:
BuildRequires:  perl(Test::Pod) >= 1.14
# Dependencies:

Provides:       perl(AppConfig)
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


%check
AUTOMATED_TESTING=1 make test


%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes README TODO
%{perl_vendorlib}/AppConfig.pm
%{perl_vendorlib}/AppConfig/
%{_mandir}/man3/AppConfig*.3*


%changelog
%autochangelog
