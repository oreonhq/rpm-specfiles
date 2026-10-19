%global source0_hash fe41e6817185c96586136be6ba4b0e1be68ddce61c44ada1f70b11d492706e99
%global cpan_version 0.090
Name:           perl-Log-Any-IfLOG
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        1%{?dist}
Summary:        Load Log::Any only if "logging is enabled"
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Any-IfLOG
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Log-Any-IfLOG-%{cpan_version}.tar.gz
BuildArch:      noarch
Requires:       perl(Log::Any)
%global __provides_exclude ^perl\\(Log::Any::IfLOG::DumbObj\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is a drop-in replacement/wrapper for Log::Any to be used from
your modules. This is a quick-hack solution to avoid the cost of loading
Log::Any under "normal condition".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Any-IfLOG-%{cpan_version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
