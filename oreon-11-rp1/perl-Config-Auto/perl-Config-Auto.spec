%global source0_hash e960e04df995852aba275cf83ac6f947e44a4139de156858c01f0cec7f7ab53f

Name:           perl-Config-Auto
Version:        0.44
Release:        34%{?dist}
Summary:        Magical config file parser
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-Auto
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Config-Auto-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Config::IniFiles)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(YAML)

%{?perl_default_filter}

%description
This module was written after having to write Yet Another Config File
Parser for some variety of colon-separated config. It searches the filesystem
for the program's configuration file, basing itself on the program's name
and returns a data structure based on the file's contents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Auto-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
