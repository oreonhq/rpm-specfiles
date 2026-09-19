%global source0_hash 598f48d7cd80bcd13ed59b816eee400eba8194a396eaf895476d792a18839557

Name:		perl-IO-FDPass
Version:	1.3
Release:	18%{?dist}
Summary:	Pass a file descriptor over a socket
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/IO-FDPass
Source0:	https://cpan.metacpan.org/modules/by-module/IO/IO-FDPass-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Canary::Stability)
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(Socket)
# Dependencies
Requires:	perl(XSLoader)

# Avoid provides from private shared objects
%{?perl_default_filter}

%description
This small low-level module only has one purpose: pass a file descriptor to
another process, using a (streaming) UNIX domain socket (on POSIX systems) or
any (streaming) socket (on WIN32 systems). The ability to pass file descriptors
on Windows is currently the unique selling point of this module. Have I
mentioned that it is really small, too?

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-FDPass-%{version}

%build
PERL_CANARY_STABILITY_NOPROMPT=1 perl Makefile.PL \
	INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc Changes README
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/
%{_mandir}/man3/IO::FDPass.3*

%changelog
%autochangelog
