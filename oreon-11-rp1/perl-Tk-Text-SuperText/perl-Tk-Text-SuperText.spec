%global source0_hash 43c67b332ea9a49b9b493f4916165efd7e01bd7f5f9a52cf1af874a9079bd10c

Name:           perl-Tk-Text-SuperText
Version:        0.12
Release:        12%{?dist}
Summary:        Improved text widget for perl/tk
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-Text-SuperText
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/Tk-Text-SuperText-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tk) >= 804.030
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Text)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)

%description
Tk::Text::SuperText implements many new features over the standard Tk::Text
widget while supporting all it's standard features. Its used simply as the
Tk::Text widget.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-Text-SuperText-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
