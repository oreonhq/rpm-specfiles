%global source0_hash 2bd440ce3d3068e99ea62f185a2e0d4bceb5dade4f1279ada41592b721ce2b56

Name:           perl-Object-Remote
Version:        0.004004
Release:        5%{?dist}
Summary:        Call methods on objects in other processes or on other hosts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Remote
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Object-Remote-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Algorithm::C3)
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::C3)
# Class::C3::next - the part of perl-Class-C3, but it isn't listed in provides
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Future) >= 0.49
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Contextual) >= 0.005
BuildRequires:  perl(Log::Contextual::Role::Router)
BuildRequires:  perl(Method::Generate::BuildAll)
BuildRequires:  perl(Method::Generate::DemolishAll)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.006
BuildRequires:  perl(Moo::HandleMoose::_TypeMap)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strictures) >= 2
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::HiRes)
# Tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
Requires:       perl(Algorithm::C3)
Requires:       perl(Class::C3)
Requires:       perl(Devel::GlobalDestruction)
Requires:       perl(Future) >= 0.49
Requires:       perl(Log::Contextual) >= 0.005
Requires:       perl(Log::Contextual::Role::Router)
Requires:       perl(Method::Generate::BuildAll)
Requires:       perl(Method::Generate::DemolishAll)
Requires:       perl(Moo) >= 1.006
Requires:       perl(Moo::HandleMoose::_TypeMap)
Requires:       perl(MRO::Compat)
Requires:       perl(strictures) >= 2
Requires:       openssh-clients
Requires:       sudo

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Future\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moo\\)$
%global __requires_exclude %__requires_exclude|^perl\\(strictures\\) >= 1$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(maybe\\)$
%global __provides_exclude %__provides_exclude|^perl\\(maybe::start\\)$
%global __provides_exclude %__provides_exclude|^perl\\(start\\)$
%global __provides_exclude %__provides_exclude|^perl\\(then\\)$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %__requires_exclude|^perl\\(ORFeed.*\\)$
%global __requires_exclude %__requires_exclude|^perl\\(ORTest.*\\)$
%global __requires_exclude %__requires_exclude|^perl\\(t::lib::.*\\)$

%description
Object::Remote allows you to create an object in another process - usually
one running on another machine you can connect to via ssh, although there
are other connection mechanisms available.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-Remote-%{version}
perl -MConfig -pi -e 's|^#!.*perl|$Config{startperl}|' bin/*

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

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
%license LICENSE
%doc Changes README
%{_bindir}/object-remote*
%{_bindir}/remoterepl
%dir %{perl_vendorlib}/Object
%{perl_vendorlib}/Object/Remote*
%{_mandir}/man3/Object::Remote*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
