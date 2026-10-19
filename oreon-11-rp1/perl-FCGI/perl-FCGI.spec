%global source0_hash 4c7d60e26da2c07f058a4e345021e92505273b33c9542215977e084611f09ecf
%bcond perl_FCGI_enables_client_tests %{undefined rhel}
Name:           perl-FCGI
Summary:        FastCGI Perl bindings
Epoch:          1
Version:        0.82
Release:        1%{?dist}
License:        OML
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/FCGI-%{version}.tar.gz
Patch0:         FCGI-0.78-CVE-2012-6687.patch
Patch1:         FCGI-0.82-Update-fcgiapp.c.patch
Patch2:         FCGI-0.82-Fix-size_t-overflow-in-Malloc-argument-in-ReadParams.patch
URL:            https://metacpan.org/release/FCGI
%if %{with perl_FCGI_enables_client_tests}
%endif
Requires:       perl(Carp)
Requires:       perl(XSLoader)
Provides:       bundled(fcgi)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FCGI::Client)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-FCGI-tests -f %{oreon_filedir}/perl-FCGI-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.82-18
- Prepare for Oreon 11 (RP1)
