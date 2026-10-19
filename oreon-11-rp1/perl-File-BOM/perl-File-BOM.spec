%global source0_hash 28edc43fcb118e11bc458c9ae889d56d388c1d9bc29997b00b1dffd8573823a3
Name:           perl-File-BOM
Version:        0.18
Release:        1%{?dist}
Summary:        Utilities for handling Byte Order Marks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-BOM
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/File-BOM-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Encode) >= 1.99
Requires:       perl(Readonly) >= 0.06
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Encode\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Readonly\\)$
# oreon:deps
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
