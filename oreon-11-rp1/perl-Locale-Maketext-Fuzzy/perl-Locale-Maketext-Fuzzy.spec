%global source0_hash 3785171ceb78cc7671319a3a6d8ced9b190e097dfcd9b2a9ebc804cd1a282f96

Name:           perl-Locale-Maketext-Fuzzy
Version:        0.11
Release:        34%{?dist}
Summary:        Maketext from already interpolated strings

License:        MIT
URL:            https://metacpan.org/release/Locale-Maketext-Fuzzy
Source0:        https://cpan.metacpan.org/modules/by-module/Locale/Locale-Maketext-Fuzzy-%{version}.tar.gz
Patch0:         Locale-Maketext-Fuzzy-0.11-Fix-building-on-Perl-without-dot-in-INC.patch

BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Locale::Maketext)
# Tests:
BuildRequires:  perl(Test::More)

%description
This module is a subclass of Locale::Maketext, with additional
support for localizing messages that already contains interpolated
variables.  This is most useful when the messages are returned by
external modules -- for example, to match "dir: command not foundr"
against "[_1]: command not found".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Locale-Maketext-Fuzzy-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Locale/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
