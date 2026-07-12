%global source0_hash 50cacbe2fffbb5c70d1ba5e9427d5c8adee618436ec73f96ed0539232e2c8b63

Name:           perl-Pod-Wrap
Version:        0.01
Release:        29%{?dist}
Summary:        Wrap pod paragraphs, leaving verbatim text and code alone
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Wrap
Source0:        https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/Pod-Wrap-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Text::Wrap)
# Tests
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Pod::Stripper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)

Provides:       perl(Pod::Wrap)
%description
This is a Pod::Parser subclass, based on Pod::Stripper. It parses perl
files, wrapping pod text, and leaving everything else intact. It prints
it's output to wherever you point it to (like you do with Pod::Parser (and
Pod::Stripper)).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Wrap-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license Artistic COPYING
%doc README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
