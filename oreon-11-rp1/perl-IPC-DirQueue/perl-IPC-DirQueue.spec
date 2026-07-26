%global source0_hash f636e8bb3f54515be77476f99fd962801d2d3f32bb43e154b459df4c64974f99

Name:           perl-IPC-DirQueue
Version:        1.0
Release:        47%{?dist}
Summary:        Disk-based many-to-many task queue
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-DirQueue
Source0:        https://cpan.metacpan.org/modules/by-module/IPC/IPC-DirQueue-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(bytes)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)

%description
This module implements a FIFO queueing infrastructure, using a directory as
the communications and storage media. No daemon process is required to
manage the queue; all communication takes place via the filesystem.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPC-DirQueue-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc BUGS CHANGES README.dist TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
