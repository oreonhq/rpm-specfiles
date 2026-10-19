%global source0_hash e9186df3706a877efd6149f2c711d6cf87dd6cf72f6ab935ba8121b225b265cb
Name:           perl-Sys-Hostname-Long
Version:        1.5
Release:        1%{?dist}
Summary:        Try every conceivable way to get full hostname
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-Hostname-Long
Source0:        https://cpan.metacpan.org/modules/by-module/Sys/Sys-Hostname-Long-%{version}.tar.gz
BuildArch:      noarch
Requires:       hostname
Requires:       perl(IO::Socket)
%global __requires_exclude_from ^%{perl_vendorlib}/Sys/Hostname/testall\.pl
Provides:       perl(Sys::Hostname::Long)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  hostname
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Attempt via many methods to get the system's full name. The Sys::Hostname
class is the best and standard way to get the system hostname. However,
it is missing the long hostname.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sys-Hostname-Long-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
perl testall.pl
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
