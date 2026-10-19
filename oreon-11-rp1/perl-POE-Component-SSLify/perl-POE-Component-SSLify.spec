%global source0_hash 1db61c1da047c96de4972b529c72a90d806991f65fd79418951a312461dc185d
%bcond_with perl_POE_Component_SSLify_enables_extra_test
Name:           perl-POE-Component-SSLify
Version:        1.012
Release:        1%{?dist}
Summary:        Makes using SSL in the world of POE easy!
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-SSLify
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/POE-Component-SSLify-%{version}.tar.gz
Patch0:         POE-Component-SSLify-1.012-Use-default-SSL-version-in-tests.patch
Patch1:         POE-Component-SSLify-1.012-Disable-sessions-tickets-with-OpenSSL-1.1.1.patch
Patch2:         POE-Component-SSLify-1.012-Adapt-to-OpenSSL-3.patch
BuildArch:      noarch
%if %{with perl_POE_Component_SSLify_enables_extra_test}
%endif
Requires:       perl(POE) >= 1.267
Requires:       perl(warnings)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((IO::Handle|Net::SSLeay|POE)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Client::TCP)
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This component represents the standard way to do SSL in POE.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(blib)
Requires:       perl(IO::Handle) >= 1.28
Requires:       perl(Net::SSLeay) >= 1.36
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n POE-Component-SSLify-%{version}
%if !%{with perl_POE_Component_SSLify_enables_extra_test}
rm t/99_mire_test.t t/apocalypse.t t/simple_parallel_superbig.t t/simple_superbig.t
perl -i -ne 'print $_ unless m{^\Qt/99_mire_test.t\E}' MANIFEST
perl -i -ne 'print $_ unless m{^\Qt/apocalypse.t\E}' MANIFEST
perl -i -ne 'print $_ unless m{^\Qt/simple_parallel_superbig.t\E}' MANIFEST
perl -i -ne 'print $_ unless m{^\Qt/simple_superbig.t\E}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a mylib t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
%if %{with perl_POE_Component_SSLify_enables_extra_test}
export AUTOMATED_TESTING=1
%else
export AUTOMATED_TESTING=0
%endif
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm -f *.list
%if %{with perl_POE_Component_SSLify_enables_extra_test}
export AUTOMATED_TESTING=1
%else
export AUTOMATED_TESTING=0
%endif
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-POE-Component-SSLify-tests -f %{oreon_filedir}/perl-POE-Component-SSLify-tests.list

%changelog

%autochangelog
