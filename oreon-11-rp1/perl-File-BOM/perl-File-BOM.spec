%global source0_hash 28edc43fcb118e11bc458c9ae889d56d388c1d9bc29997b00b1dffd8573823a3

Name:           perl-File-BOM
Version:        0.18
Release:        17%{?dist}
Summary:        Utilities for handling Byte Order Marks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-BOM
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/File-BOM-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 1.99
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Readonly) >= 0.06
BuildRequires:  perl(Symbol)
# Tests only
# Required to process t/testrules.yml
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Exception) >= 0.20
BuildRequires:  perl(Test::More) >= 0.10
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(utf8)
Requires:       perl(Encode) >= 1.99
Requires:       perl(Readonly) >= 0.06

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Encode\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Readonly\\)$

%description
This module provides functions for handling Unicode byte order marks, which
are to be found at the beginning of some files and streams.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-BOM-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
