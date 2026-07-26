%global source0_hash 8afa3a8fff8eb1b29d646ed188a2cc889b19d5a0fb3aa5ddad508ccb0c79bdf2

Name:           perl-CGI-Fast
Version:        2.17
Release:        7%{?dist}
Summary:        CGI Interface for Fast CGI
# lib/CGI/Fast.pm probably qotes piece of Artistic license before declaring
# "as Perl itself" <https://github.com/leejo/cgi-fast/issues/13>
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Fast
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-Fast-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(CGI) >= 4.00
BuildRequires:  perl(CGI::Carp)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(FCGI) >= 0.67
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(warnings)
Requires:       perl(deprecate)
Requires:       perl(CGI) >= 4.00
Requires:       perl(FCGI) >= 0.67
# perl-CGI-Fast was split from perl-CGI
Conflicts:      perl-CGI < 4.00

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((CGI|FCGI)\\)$

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%description
CGI::Fast is a subclass of the CGI object created by CGI.pm. It is
specialized to work well FCGI module, which greatly speeds up CGI scripts
by turning them into persistently running server processes. Scripts that
perform time-consuming initialization processes, such as loading large
modules or opening persistent database connections, will see large
performance improvements.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Fast-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

# Remove release test
rm t/006_changes.t
perl -i -ne 'print $_ unless m{^t/006_changes\.t}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
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
%doc Changes README
%{perl_vendorlib}/CGI*
%{_mandir}/man3/CGI::Fast*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
