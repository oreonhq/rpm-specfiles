%global source0_hash b7edfdbc175f6ff1b4f5618983c81534e1e415156c6d21a7f2c19496ee392276
%bcond_without perl_Log_Log4perl_Appender_Socket_UNIX_enables_optional_test
Name:       perl-Log-Log4perl-Appender-Socket-UNIX
Version:    1.04
Release:        34%{?dist}
Summary:        Log4perl appender for writing to UNIX domain sockets
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/Log-Log4perl-Appender-Socket-UNIX
Source0:        https://cpan.metacpan.org/modules/by-module/Log/Log-Log4perl-Appender-Socket-UNIX-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Log_Log4perl_Appender_Socket_UNIX_enables_optional_test}
%endif
Requires:       perl(Log::Log4perl::Appender)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Log::Log4perl::Appender)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a simple appender for writing to a unix domain socket. It relies on
Socket and only logs to an existing socket.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Log_Log4perl_Appender_Socket_UNIX_enables_optional_test}
Requires:       perl(Test::NoWarnings)
%endif
Requires:       perl(warnings)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Log4perl-Appender-Socket-UNIX-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
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
%files -n perl-Log-Log4perl-Appender-Socket-UNIX-tests -f %{oreon_filedir}/perl-Log-Log4perl-Appender-Socket-UNIX-tests.list

%changelog

%autochangelog
