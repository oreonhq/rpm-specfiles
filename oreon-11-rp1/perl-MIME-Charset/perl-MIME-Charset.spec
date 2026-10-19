%global source0_hash 1bb7a6e0c0d251f23d6e60bf84c9adefc5b74eec58475bfee4d39107e60870f0
%bcond perl_MIME_Charset_enables_optional_test %{undefined rhel}
Name:           perl-MIME-Charset
Version:        1.013.1
Release:        10%{?dist}
Summary:        Charset Informations for MIME
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-Charset
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-Charset-%{version}.tar.gz
Patch0:         MIME-Charset-1.012-Do-not-install-modules-from-the-Internet.patch
BuildArch:      noarch
%if %{with perl_MIME_Charset_enables_optional_test}
%endif
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MIME::Charset\\)$
Provides:       perl(MIME::Charset)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode::EUCJPASCII)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Win32)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MIME::Charset provides information about character sets used for MIME
messages on Internet.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MIME-Charset-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf ./inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.013.1-10
- Prepare for Oreon 11 (RP1)
