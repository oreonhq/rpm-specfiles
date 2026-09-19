%global source0_hash 26c321a43c4d1843558b39ea6f6c70c6dbc96976249424bf770a229ee31f20f3

Name:           perl-Net-Daemon
Version:        0.49
Release:        17%{?dist}
Summary:        Perl extension for portable daemons

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Daemon
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/Net-Daemon-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
%{?_with_network_tests:
BuildRequires:  perl(Sys::Syslog)
}
# Thread not used at tests
# threads not used at tests
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# Network tests:
%{?_with_network_tests:
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(lib)
BuildRequires:  perl(Socket)
}
Suggests:       perl(Sys::Syslog)
# threads is prefered over Threads
Suggests:       perl(threads)
Requires:       perl(threads::shared)

%{?perl_default_filter}

%description
Net::Daemon is an abstract base class for implementing portable server 
applications in a very simple way. The module is designed for Perl 5.006 and 
ithreads (and higher), but can work with fork() and Perl 5.004.

The Net::Daemon class offers methods for the most common tasks a daemon 
needs: Starting up, logging, accepting clients, authorization, restricting 
its own environment for security and doing the true work. You only have to 
override those methods that aren't appropriate for you, but typically 
inheriting will safe you a lot of work anyways.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Daemon-%{version}
# Convert EOL
/usr/bin/sed -i 's/\r//' README

# generate our other two licenses...
/usr/bin/perldoc perlgpl > LICENSE.GPL
/usr/bin/perldoc perlartistic > LICENSE.Artistic

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?!_with_network_tests:
# Disable tests which will fail under mock
  rm t/config*
  rm t/fork*
  rm t/ithread*
  rm t/loop*
  rm t/single.t
  rm t/unix.t
}

%{make_build} test

%files
%doc ChangeLog README
%license LICENSE.*
%{perl_vendorlib}/Net*
%{_mandir}/man3/Net*.3*

%changelog
%autochangelog
