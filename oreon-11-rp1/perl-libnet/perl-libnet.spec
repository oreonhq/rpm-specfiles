%global source0_hash a71f4db580e1a767d6936faa5baf38f1fa617824342da078b561283e86f8f4a2
%global base_version 3.15
%bcond_with perl_libnet_enables_optional_test
%bcond_without perl_libnet_enables_sasl
%bcond_without perl_libnet_enables_ssl
Name:           perl-libnet
Version:        3.15
Release:        1%{?dist}
Summary:        Perl clients for various network protocols
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/libnet
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHAY/libnet-%{version}.tar.gz
Patch0:         libnet-3.09-Normalize-Changes-encoding.patch
Patch1:         libnet-3.08-Do-not-create-Net-libnet.cfg.patch
BuildArch:      noarch
%if %{with perl_libnet_enables_ssl} && !%{defined perl_bootstrap}
%endif
%if %{with perl_libnet_enables_optional_test}
%if %{with perl_libnet_enables_ssl} && !%{defined perl_bootstrap}
%endif
%endif
Requires:       perl(File::Basename)
Requires:       perl(IO::Socket) >= 1.05
Requires:       perl(IO::Socket::IP) >= 0.25
Requires:       perl(POSIX)
Requires:       perl(Socket) >= 2.016
%if %{with perl_libnet_enables_sasl} && !%{defined perl_bootstrap}
Suggests:       perl(Authen::SASL)
Suggests:       perl(MIME::Base64)
%endif
Requires:       perl(Digest::MD5)
%if %{with perl_libnet_enables_ssl} && !%{defined perl_bootstrap}
Suggests:       perl(IO::Socket::SSL) >= 2.007
%endif
Conflicts:      perl < 4:5.22.0-347
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((IO::Socket|Socket)\\)$
Provides:       perl(Net::Config)
Provides:       perl(Net::Domain)
Provides:       perl(Net::FTP)
Provides:       perl(Net::NNTP)
Provides:       perl(Net::SMTP)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a collection of Perl modules which provides a simple and
consistent programming interface (API) to the client side of various
protocols used in the internet community.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libnet-%{base_version}
%patch -P0 -p1
%patch -P1 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 </dev/null
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.15-522
- Prepare for Oreon 11 (RP1)
