%global source0_hash 88a9b2df69e769e5855a408b19f61915b82e8fe070ab5cf4d525dd3b8bbe31c1

Name:           perl-Net-SCP
Version:        0.08
Release:        49%{?dist}
Summary:        Perl extension for secure copy protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-SCP
Source0:        https://cpan.metacpan.org/authors/id/I/IV/IVAN/Net-SCP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Net::SSH)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(vars)
# Tests only
# -
Requires:       openssh-clients

%description
This module implements a Perl interface to scp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-SCP-%{version}
chmod 644 -c Changes README SCP.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
