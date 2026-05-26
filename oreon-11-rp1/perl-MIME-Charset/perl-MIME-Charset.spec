%bcond perl_MIME_Charset_enables_optional_test %{undefined rhel}

Name:           perl-MIME-Charset
Version:        1.013.1
Release:        10%{?dist}
Summary:        Charset Informations for MIME
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-Charset
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-Charset-%{version}.tar.gz
# Disable Module::AutoInstall
Patch0:         MIME-Charset-1.012-Do-not-install-modules-from-the-Internet.patch
# oreon url source checksums begin
%global source0_sha256 1bb7a6e0c0d251f23d6e60bf84c9adefc5b74eec58475bfee4d39107e60870f0
%global source0_file MIME-Charset-1.013.1.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Win32)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Optional run-time:
%if %{with perl_MIME_Charset_enables_optional_test}
# Encode::DIN66003 0.01 not needed at tests
BuildRequires:  perl(Encode::EUCJPASCII) >= 0.02
%endif
# Encode::HanExtra 0.20 not needed at tests
# Encode::JISX0213 0.03 not yet packaged
# Tests:
# Encode::CN not used
# Encode::JP not used
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00

# Filter under-specified symbols
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MIME::Charset\\)$

%description
MIME::Charset provides information about character sets used for MIME
messages on Internet.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/MIME-Charset-1.013.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1bb7a6e0c0d251f23d6e60bf84c9adefc5b74eec58475bfee4d39107e60870f0" || { echo "oreon: Source0 SHA256 mismatch for MIME-Charset-1.013.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

%check
make test

%files
%license ARTISTIC COPYING
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.013.1-10
- Prepare for Oreon 11 (RP1)
