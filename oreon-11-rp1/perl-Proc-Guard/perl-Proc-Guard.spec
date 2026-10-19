%global source0_hash 6feae8bce21c1dcdd1baa636d5f87be29084e827b338194f672b23197b4150a4
Name:           perl-Proc-Guard
Version:        0.07
Release:        1%{?dist}
Summary:        Process runner with RAII pattern
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-Guard
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Proc-Guard-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Exporter) >= 5.63
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)$
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Proc::Guard runs process, and destroys it when the perl script exits.
This is useful for testing code working with server process.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Proc-Guard-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
