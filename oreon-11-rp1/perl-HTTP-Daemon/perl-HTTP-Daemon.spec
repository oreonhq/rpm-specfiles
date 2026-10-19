%global source0_hash 16281580c40e23108d028434698b5d7d53637bf904c9df822481e253cbec920c
%{bcond_without perl_HTTP_Daemon_enables_optional_test}
Name:           perl-HTTP-Daemon
Version:        6.17
Release:        1%{?dist}
Summary:        Simple HTTP server class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Daemon
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Daemon-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_HTTP_Daemon_enables_optional_test} && !%{defined %perl_bootstrap}
%endif
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Response) >= 6
Requires:       perl(HTTP::Status) >= 6
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(LWP::MediaTypes) >= 6
Conflicts:      perl-libwww-perl < 6
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTTP::(Date|Request|Response|Status)|IO::Socket::IP|LWP::MediaTypes\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestServer|TestServer::(BasicTests|Reflect)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(TestServer|TestServer::(BasicTests|Reflect)\\)$
Provides:       perl(HTTP::Daemon)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(LWP::MediaTypes)
BuildRequires:  perl(LWP::RobotUA)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(URI)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Instances of the HTTP::Daemon class are HTTP/1.1 servers that listen on a
socket for incoming requests. The HTTP::Daemon is a subclass of
IO::Socket::IP, so you can perform socket operations directly on it too.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(LWP::RobotUA)
Requires:       perl(LWP::UserAgent) >= 6.37
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n HTTP-Daemon-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-HTTP-Daemon-tests -f %{oreon_filedir}/perl-HTTP-Daemon-tests.list

%changelog

%autochangelog
