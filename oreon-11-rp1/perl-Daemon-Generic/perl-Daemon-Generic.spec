%global source0_hash 3ac3ff8e6bdc494ef40ee4147adf28c7bbcabc6e58dea70aa4411d0e00df900f

Name:           perl-Daemon-Generic
Version:        0.85
Release:        27%{?dist}
Summary:        Framework to provide start/stop/reload for a daemon
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Daemon-Generic
Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/Daemon-Generic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Carp)
# Cwd - not used for tests
BuildRequires:  perl(Eval::LineNumbers)
BuildRequires:  perl(Event)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# File::Basename - not used for tests
BuildRequires:  perl(File::Flock)
BuildRequires:  perl(File::Flock::Forking)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
# Text::Wrap - not used for tests
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
Requires:       perl(Cwd)
Requires:       perl(File::Basename)
Requires:       perl(Text::Wrap)
Requires:       perl(Time::HiRes)

%{?perl_default_filter}

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

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Daemon*
%{_mandir}/man3/Daemon*

%changelog
%autochangelog
