%global source0_hash edf915d6cc66bee43503aa6dc2b373366f38eaff701582183dad10cb8adf2972
Name:           perl-IO-Socket-Timeout
Version:        0.32
Release:        31%{?dist}
Summary:        IO::Socket with read/write timeout
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Socket-Timeout
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Socket-Timeout-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(PerlIO::via::Timeout) >= 0.32
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(PerlIO::via::Timeout\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PerlIO::via::Timeout)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
IO::Socket provides a way to set a timeout on the socket, but the timeout
will be used only for connection, not for reading / writing operations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Socket-Timeout-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
