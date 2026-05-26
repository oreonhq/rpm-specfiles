%if ! (0%{?rhel})
%{bcond_without perl_IO_Socket_INET6_enables_optional_test}
%else
%{bcond_with perl_IO_Socket_INET6_enables_optional_test}
%endif

Name:           perl-IO-Socket-INET6
Version:        2.73
Release:        12%{?dist}
Summary:        Perl Object interface for AF_INET|AF_INET6 domain sockets
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Socket-INET6
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/IO-Socket-INET6-2.73.tar.gz

# Fix bad code in test. Original code hides error, related to BZ#1207174
Patch0:         IO-Socket-INET6-2.72-fix_die_in_test.patch
# Fix random test error in binding to socket BZ#1207174
Patch1:         IO-Socket-INET6-2.72-bz1207174-fix_random_test_error.patch
# oreon url source checksums begin
%global source0_sha256 b6da746853253d5b4ac43191b4f69a4719595ee13a7ca676a8054cf36e6d16bb
%global source0_file IO-Socket-INET6-2.73.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6) >= 0.12
BuildRequires:  perl(strict)
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
%if %{with perl_IO_Socket_INET6_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::TrailingSpace)
%endif
# Runtime

%description
Perl Object interface for AF_INET|AF_INET6 domain sockets.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/IO-Socket-INET6-2.73.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b6da746853253d5b4ac43191b4f69a4719595ee13a7ca676a8054cf36e6d16bb" || { echo "oreon: Source0 SHA256 mismatch for IO-Socket-INET6-2.73.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n IO-Socket-INET6-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc ChangeLog README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::Socket::INET6.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.73-12
- Prepare for Oreon 11 (RP1)
