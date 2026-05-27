%global source0_hash a71f4db580e1a767d6936faa5baf38f1fa617824342da078b561283e86f8f4a2

%global base_version 3.15

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_libnet_enables_optional_test
%else
%bcond_with perl_libnet_enables_optional_test
%endif
# SASL support
%bcond_without perl_libnet_enables_sasl
# SSL support
%bcond_without perl_libnet_enables_ssl

Name:           perl-libnet
Version:        3.15
Release:        522%{?dist}
Summary:        Perl clients for various network protocols
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/libnet
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHAY/libnet-%{base_version}.tar.gz
# Convert Changes to UTF-8
Patch0:         libnet-3.09-Normalize-Changes-encoding.patch
# Do not create Net/libnet.cfg, bug #1238689
Patch1:         libnet-3.08-Do-not-create-Net-libnet.cfg.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Getopt::Std not used because of Do-not-create-Net-libnet.cfg.patch
# IO::File not used because of Do-not-create-Net-libnet.cfg.patch
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
# Convert::EBCDIC not used
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
# File::Basename not used at tests
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket) >= 1.05
# Prefer IO::Socket::IP over IO::Socket::INET6 and IO::Socket::INET
# IO::Socket::INET6 not used
BuildRequires:  perl(IO::Socket::IP) >= 0.25
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket) >= 2.016
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Time::Local)
# Optional run-time:
# Authen::SASL not used at tests
# Digest::MD5 not used at tests
%if %{with perl_libnet_enables_ssl} && !%{defined perl_bootstrap}
# Core modules must be built without non-core dependencies
BuildRequires:  perl(IO::Socket::SSL) >= 2.007
%endif
# MD5 not used because we prefer Digest::MD5
# MIME::Base64 not used at tests
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More)
%if %{with perl_libnet_enables_optional_test}
# Optional tests:
%if %{with perl_libnet_enables_ssl} && !%{defined perl_bootstrap}
# Core modules must be built without non-core dependencies
BuildRequires:  perl(IO::Socket::SSL::Utils)
%endif
%endif
Requires:       perl(File::Basename)
Requires:       perl(IO::Socket) >= 1.05
# Prefer IO::Socket::IP over IO::Socket::INET6 and IO::Socket::INET
Requires:       perl(IO::Socket::IP) >= 0.25
Requires:       perl(POSIX)
Requires:       perl(Socket) >= 2.016
# Optional run-time:
# Core modules must be built without non-core dependencies
%if %{with perl_libnet_enables_sasl} && !%{defined perl_bootstrap}
Suggests:       perl(Authen::SASL)
Suggests:       perl(MIME::Base64)
%endif
# Digest::MD5 or MD5
Requires:       perl(Digest::MD5)
%if %{with perl_libnet_enables_ssl} && !%{defined perl_bootstrap}
Suggests:       perl(IO::Socket::SSL) >= 2.007
%endif
Conflicts:      perl < 4:5.22.0-347

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((IO::Socket|Socket)\\)$

%description
This is a collection of Perl modules which provides a simple and
consistent programming interface (API) to the client side of various
protocols used in the internet community.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n libnet-%{base_version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 </dev/null
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license Artistic Copying LICENCE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.15-522
- Prepare for Oreon 11 (RP1)
