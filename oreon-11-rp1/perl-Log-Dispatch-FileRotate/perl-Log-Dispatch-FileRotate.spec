%global source0_hash b55d6cede3f0a06426488fbfa554f4561320b014c1023893ced29508e5bce4ec
Name:           perl-Log-Dispatch-FileRotate
Version:        1.38
Release:        13%{?dist}
Summary:        Log to files that archive/rotate themselves
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Dispatch-FileRotate
Source0:        https://cpan.metacpan.org/modules/by-module/Log/Log-Dispatch-FileRotate-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Log::Dispatch) >= 2.60
Requires:       perl(version)
Provides:       perl(Log::Dispatch::FileRotate)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Dispatch::Output)
BuildRequires:  perl(Log::Dispatch::Screen)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a simple object for logging to files under the
Log::Dispatch::* system, and automatically rotating them according to
different constraints. This is basically a Log::Dispatch::File wrapper
with additions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Log-Dispatch-FileRotate-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} -c $RPM_BUILD_ROOT
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
