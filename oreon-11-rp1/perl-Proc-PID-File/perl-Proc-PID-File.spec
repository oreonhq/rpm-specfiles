%global source0_hash 3bceda49df182d3d8168b70c2a51b2056f2fd45950a6d0428a9992fd355cd4a4

Name:           perl-Proc-PID-File
Version:        1.29
Release:        23%{?dist}
Summary:        Module to manage process id files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later

URL:            https://metacpan.org/release/Proc-PID-File
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMITRI/Proc-PID-File-%{version}.tar.gz
Patch0:         perl-Proc-PID-File-1.29-undef.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(threads)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  procps-ng
Requires:       procps-ng

%{?perl_default_filter}

%description
This Perl module is useful for writers of daemons and other processes that
need to tell whether they are already running, in order to prevent multiple
process instances.  The module accomplishes this via *nix-style I<pidfiles>,
which are files that store a process identifier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Proc-PID-File-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc README Changes
%{perl_vendorlib}/Proc
%{_mandir}/man3/Proc*

%changelog
%autochangelog
