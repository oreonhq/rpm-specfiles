%global source0_hash 65ad57eabc53a85e2b7c6146136969d26f2d3639d8ae4c486beea5982041e860
Name:           perl-Child
Version:        0.013
Release:        1%{?dist}
Summary:        Object oriented simple interface to fork()
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Child
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Child-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Exporter) >= 5.57
Requires:       perl(POSIX)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Fork is too low level and difficult to manage. Often people forget to exit
at the end, reap their children, and check exit status. The problem is the
low level functions provided to do these things. Throw in pipes for IPC and
you just have a pile of things nobody wants to think about.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Child-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
