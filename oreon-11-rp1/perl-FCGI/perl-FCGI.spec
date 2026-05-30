%global source0_hash 4c7d60e26da2c07f058a4e345021e92505273b33c9542215977e084611f09ecf

# Perform functional tests using FCGI::Client.
# RHEL does not include FCGI::Client due to its dependencies.
%bcond perl_FCGI_enables_client_tests %{undefined rhel}

Name:           perl-FCGI
Summary:        FastCGI Perl bindings
# needed to properly replace/obsolete fcgi-perl
Epoch:          1
Version:        0.82
Release:        18%{?dist}
# eg/echo.pl:   "See the LICENSE file"
# fastcgi.h:    "See the LICENSE file"
# FCGI.pm:      "See the LICENSE file"
# fcgiapp.c:    "See the LICENSE file"
# fcgiapp.h:    "See the LICENSE file"
# fcgimisc.h:   "See the LICENSE file
# fcgios.h:     "See the LICENSE file"
# LICENSE:      OML
# os_unix.c:    "See the LICENSE file"
# README:       "See the LICENSE file"
## Used at build time, but nonpackaged
# configure:    FSFUL
## Unused and nonpackaged
# os_win32.c:   "See the LICENSE file"
License:        OML
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/FCGI-%{version}.tar.gz
# Fix CVE-2012-6687 in the bundled fcgi library, bug #1190294, CPAN RT#118405,
# patch copied from Debian's libfcgi-perl.
Patch0:         FCGI-0.78-CVE-2012-6687.patch
# 1/2 Fix CVE-2025-40907 in the bundled fcgi library, bug #2366847,
# <https://github.com/perl-catalyst/FCGI/issues/14>, copied from fcgi2 library
# <https://github.com/FastCGI-Archives/fcgi2/issues/67>.
Patch1:         FCGI-0.82-Update-fcgiapp.c.patch
# 2/2 Fix CVE-2025-40907 in the bundled fcgi library, bug #2366847,
# <https://github.com/perl-catalyst/FCGI/issues/14>, copied from fcgi2 library
# <https://github.com/FastCGI-Archives/fcgi2/issues/67>.
Patch2:         FCGI-0.82-Fix-size_t-overflow-in-Malloc-argument-in-ReadParams.patch
URL:            https://metacpan.org/release/FCGI
# bash for sh executed from Makefile.PL
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
# grep executed by configure
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
# ExtUtils::Liblist not used
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
# File::Spec not used on Linux
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
# sed executed by configure
BuildRequires:  sed
# Run-time:
# Carp not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test)
%if %{with perl_FCGI_enables_client_tests}
BuildRequires:  perl(FCGI::Client)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
%endif
Requires:       perl(Carp)
Requires:       perl(XSLoader)
# fcgiapp.c, os_unix.c, os_win32.c are copied and modified from FastCGI
# Developer's Kit of an unknown version, bug #736612
Provides:       bundled(fcgi)

%{?perl_default_filter}

%description
The perl-FCGI package provides a Perl module for writing FastCGI applications.
FastCGI is a more efficient alternative to traditional CGI, as it keeps
application processes persistent across multiple requests. This module allows
Perl web applications to handle requests faster and with lower resource
overhead, making it suitable for high-traffic environments.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n FCGI-%{version}
find . -type f -exec chmod -c -x {} +
%if %{without perl_FCGI_enables_client_tests}
rm -f t/02-unix_domain_socket.t
perl -i -ne 'print $_ unless m{^t/02-unix_domain_socket\.t}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 \
                 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc ChangeLog eg README
%{perl_vendorarch}/auto/FCGI
%{perl_vendorarch}/FCGI.pm
%{_mandir}/man3/FCGI.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.82-18
- Prepare for Oreon 11 (RP1)
