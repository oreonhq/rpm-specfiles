%global source0_hash fe41e6817185c96586136be6ba4b0e1be68ddce61c44ada1f70b11d492706e99

%global cpan_version 0.090

Name:           perl-Log-Any-IfLOG
# Keep 2-digit precision
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        21%{?dist}
Summary:        Load Log::Any only if "logging is enabled"
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Any-IfLOG
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Log-Any-IfLOG-%{cpan_version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# XXX: BuildRequires:  perl(Log::Any)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       perl(Log::Any)

# Log::Any::IfLOG::DumbObj is a private module
# perl-generators don't pick it up but that may change in the future --
# better have a filter in place and be ready
%global __provides_exclude ^perl\\(Log::Any::IfLOG::DumbObj\\)$

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
