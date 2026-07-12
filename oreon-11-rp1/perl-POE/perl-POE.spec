%global source0_hash 57de2b635b15fa3a31a9e55dd51122149e5414e1158ee82235062634ee18a693

# Perform network tests
%bcond_without perl_POE_enables_network_test
# Perform optional tests
%bcond_without perl_POE_enables_optional_test

Name:       perl-POE
Version:    1.370
Release:    13%{?dist}
Summary:    Portable multitasking and networking framework for event loops
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/POE
Source0:    https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec) >= 0.87
# Getopt::Long not used
BuildRequires:  perl(lib)
BuildRequires:  perl(Socket) >= 1.7
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
# Curses 1.08 not used at tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno) >= 1.09
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Handle) >= 1.27
BuildRequires:  perl(IO::Pipely) >= 0.005
BuildRequires:  perl(IO::Poll) >= 0.01
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(IO::Tty) >= 1.08
BuildRequires:  perl(POSIX) >= 1.02
BuildRequires:  perl(Scalar::Util)
# Socket6 not needed with current Socket
# Socket::GetAddrInfo not needed with current Socket
# Storable || FreezeThaw || YAML
BuildRequires:  perl(Storable) >= 2.26
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::Cap) >= 1.10
BuildRequires:  perl(Term::ReadKey) >= 2.21
# Time::Hires loaded from lib/POE/Resource/Clock.pm
BuildRequires:  perl(Time::HiRes) >= 1.59
BuildRequires:  perl(URI) >= 1.30
# Win32* not needed
# Optional run-time:
BuildRequires:  perl(Compress::Zlib) >= 1.33
# POE::XS::Queue::Array not needed, to exhibit a default implementation
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
%if %{with perl_POE_enables_network_test}
BuildRequires:  perl(List::Util)
%endif
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::HiRes) >= 1.59
%if %{with perl_POE_enables_optional_test}
# Optional tests:
%if !%{defined perl_bootstrap}
BuildRequires:  perl(POE::Test::Loops) >= 1.360
%endif
BuildRequires:  perl(YAML)
%endif
Requires:       perl(bytes)
Recommends:     perl(Compress::Zlib) >= 1.33
Requires:       perl(Curses) >= 1.08
Requires:       perl(Data::Dumper)
Requires:       perl(Errno) >= 1.09
Requires:       perl(File::Spec) >= 0.87
Requires:       perl(IO::Handle) >= 1.27
Requires:       perl(IO::Pipely) >= 0.005
Requires:       perl(IO::Pty)
Requires:       perl(IO::Tty) >= 1.08
Suggests:       perl(POE::XS::Queue::Array)
Requires:       perl(POSIX) >= 1.02
Requires:       perl(Socket) >= 1.7
Requires:       perl(Storable) >= 2.26
Requires:       perl(Term::Cap) >= 1.10
Requires:       perl(Term::ReadKey) >= 2.21
Requires:       perl(Time::HiRes) >= 1.59

%{?perl_default_filter}
# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Curses|Errno|File::Spec|IO::Handle|IO::Pipely|IO::Pty|POSIX|Socket|Term::Cap|Term::ReadKey)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(POE::Kernel\\)$

Provides:       perl(POE)
Provides:       perl(POE::Component::Client::TCP)
Provides:       perl(POE::Component::Server::TCP)
Provides:       perl(POE::Driver::SysRW)
Provides:       perl(POE::Filter::Block)
Provides:       perl(POE::Filter::Line)
Provides:       perl(POE::Filter::Map)
Provides:       perl(POE::Pipe::TwoWay)
Provides:       perl(POE::Wheel::FollowTail)
Provides:       perl(POE::Wheel::ListenAccept)
Provides:       perl(POE::Wheel::SocketFactory)
%description
POE is a framework for cooperative, event driven multitasking in Perl. It
provides a unified interface for several event loops, including select(),
IO::Poll, Glib, Gtk, Tk, Wx, and Gtk2. Many of these event loop interfaces
were written by others, with the help of POE::Test::Loops.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n POE-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 --default
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%if !%{with perl_POE_enables_network_test}
rm run_network_tests
%endif
# note that there are currently a number of tests that throw errors, but do
# not fail nor cause the build/suite to fail.  For now just please be aware
# that there will be some noisy output as the tests are run.
# Reported upstream at http://rt.cpan.org/Public/Bug/Display.html?id=19878
unset AUTOMATED_TESTING CONTENT_LENGTH CONTENT_TYPE POE_ASSERT_USAGE \
    POE_CATCH_EXCEPTIONS POE_EVENT_LOOP POE_IMPLEMENTATION POE_USE_HIRES \
    POE_USE_SIGNAL_PIPE QUERY_STRING RELEASE_TESTING REQUEST_METHOD
make test

%files
%doc CHANGES examples HISTORY README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
