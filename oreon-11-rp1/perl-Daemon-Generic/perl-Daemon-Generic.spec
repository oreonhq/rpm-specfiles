%global source0_hash 3ac3ff8e6bdc494ef40ee4147adf28c7bbcabc6e58dea70aa4411d0e00df900f
Name:           perl-Daemon-Generic
Version:        0.85
Release:        27%{?dist}
Summary:        Framework to provide start/stop/reload for a daemon
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Daemon-Generic
Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/Daemon-Generic-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Cwd)
Requires:       perl(File::Basename)
Requires:       perl(Text::Wrap)
Requires:       perl(Time::HiRes)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Eval::LineNumbers)
BuildRequires:  perl(Event)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Flock)
BuildRequires:  perl(File::Flock::Forking)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Daemon::Generic provides a framework for starting, stopping, reconfiguring
daemon-like programs. The framework provides for standard commands that
work for as init.d files and as apachectl-like commands.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Daemon-Generic-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
