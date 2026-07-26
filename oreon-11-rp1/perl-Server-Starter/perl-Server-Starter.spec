%global source0_hash 676dc0d6cff4648538332c63c32fb88ad09ed868213ea9e62e3f19fad41b9c40

Name:           perl-Server-Starter
Version:        0.35
Release:        19%{?dist}
Summary:        Superdaemon for hot-deploying server programs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Server-Starter
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Server-Starter-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# For the tests
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Test::TCP) >= 2.08
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::SharedFork)

%package start_server
Summary:        perl-Server-Starter start_server script
Requires:       perl-Server-Starter = %{version}-%{release}

%description
It is often a pain to write a server program that supports graceful
restarts, with no resource leaks. Server::Starter, solves the problem by
splitting the task into two. One is start_server, a script provided as a
part of the module, which works as a superdaemon that binds to zero or
more TCP ports, and repeatedly spawns the server program that actually
handles the necessary tasks (for example, responding to incoming
connections). The spawned server programs under Server::Starter call
accept(2) and handle the requests.

%description start_server
perl-Server-Starter's start_server script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Server-Starter-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files start_server
%{_bindir}/start_server
%{_mandir}/man1/start_server.*

%changelog
%autochangelog
