%global source0_hash 3aca4e2a46b5c01498a446607a73f2c9121118a58cd670b3df285b6bca0d3f1c
%global pkgname Proc-Queue
Name:           perl-Proc-Queue
Version:        1.23
Release:        34%{?dist}
Summary:        Limit the number of child processes running
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-Queue
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(POSIX)
Requires:       perl(Time::HiRes)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module lets you parallelise a perl program using the fork, exit, wait
and waitpid calls as usual but without taking care of creating too many
processes and overloading the machine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 README > README.new && \
touch -r README README.new && \
mv README.new README

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
