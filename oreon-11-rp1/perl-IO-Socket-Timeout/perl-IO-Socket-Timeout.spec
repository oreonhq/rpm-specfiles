%global source0_hash edf915d6cc66bee43503aa6dc2b373366f38eaff701582183dad10cb8adf2972

Name:           perl-IO-Socket-Timeout
Version:        0.32
Release:        31%{?dist}
Summary:        IO::Socket with read/write timeout
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Socket-Timeout
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Socket-Timeout-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(PerlIO::via::Timeout) >= 0.32
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::TCP)
# Dependencies
Requires:       perl(PerlIO::via::Timeout) >= 0.32

# Filter under-specified dependencies
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(PerlIO::via::Timeout\\)$

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

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::Socket::Timeout.3*

%changelog
%autochangelog
