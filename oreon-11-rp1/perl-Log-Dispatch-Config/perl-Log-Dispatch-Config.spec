%global source0_hash 5a48c583dc87b079bf143a07fa6a73832ff02935617e21578269bc4959130b04
Name:           perl-Log-Dispatch-Config
Summary:        Log4j for Perl
Version:        1.04
Release:        40%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl        
URL:            https://metacpan.org/release/Log-Dispatch-Config
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Log-Dispatch-Config-%{version}.tar.gz
Patch0:         Log-Dispatch-Config-1.04-Adjust-tests-to-Log-Dispatch-2.47.patch
BuildArch:      noarch
Requires:       perl(AppConfig) >= 1.52
Requires:       perl(Carp)
Requires:       perl(POSIX)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(AppConfig\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(AppConfig)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Log::Dispatch::Config is a subclass of Log::Dispatch and provides a way to
configure Log::Dispatch object with configuration file (default, in AppConfig
format).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Dispatch-Config-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
