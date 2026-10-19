%global source0_hash 57de2b635b15fa3a31a9e55dd51122149e5414e1158ee82235062634ee18a693
%bcond_without perl_POE_enables_network_test
%bcond_without perl_POE_enables_optional_test
Name:       perl-POE
Version:    1.370
Release:        1%{?dist}
Summary:        Portable multitasking and networking framework for event loops
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/POE
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-%{version}.tar.gz
BuildArch:  noarch
%if %{with perl_POE_enables_network_test}
%endif
%if %{with perl_POE_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
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
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipely)
BuildRequires:  perl(IO::Poll)
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(IO::Tty)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POE::Test::Loops)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::Cap)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%if !%{with perl_POE_enables_network_test}
rm run_network_tests
%endif
unset AUTOMATED_TESTING CONTENT_LENGTH CONTENT_TYPE POE_ASSERT_USAGE \
    POE_CATCH_EXCEPTIONS POE_EVENT_LOOP POE_IMPLEMENTATION POE_USE_HIRES \
    POE_USE_SIGNAL_PIPE QUERY_STRING RELEASE_TESTING REQUEST_METHOD
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
