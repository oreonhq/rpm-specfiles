%global source0_hash 5c857dbce586f57fa3d7c4ebd320023ab3b2963b2049428ae01bd3bc4f215725

Name:           perl-Text-Aligner
Version:        0.16
Release:        17%{?dist}
Summary:        Text::Aligner Perl module
License:        ISC
URL:            https://metacpan.org/release/Text-Aligner
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Text-Aligner-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Term::ANSIColor) >= 2.02
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Term::ANSIColor\\)$

%description
Text::Aligner exports a single function, align(), which is used to justify
strings to various alignment styles. The alignment specification is the
first argument, followed by any number of scalars which are subject to
alignment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Aligner-%{version}
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
