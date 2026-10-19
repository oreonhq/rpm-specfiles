%global source0_hash 2bd440ce3d3068e99ea62f185a2e0d4bceb5dade4f1279ada41592b721ce2b56
Name:           perl-Object-Remote
Version:        0.004004
Release:        1%{?dist}
Summary:        Call methods on objects in other processes or on other hosts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Remote
Source0:        https://cpan.metacpan.org/authors/id/E/EH/EHUELS/Object-Remote-%{version}.tar.gz
BuildArch:      noarch
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
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %__requires_exclude|^perl\\(ORFeed.*\\)$
%global __requires_exclude %__requires_exclude|^perl\\(ORTest.*\\)$
%global __requires_exclude %__requires_exclude|^perl\\(t::lib::.*\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Algorithm::C3)
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::C3)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Future)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Contextual)
BuildRequires:  perl(Log::Contextual::Role::Router)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Method::Generate::BuildAll)
BuildRequires:  perl(Method::Generate::DemolishAll)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::HandleMoose::_TypeMap)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(strictures)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%files -n perl-Object-Remote-tests -f %{oreon_filedir}/perl-Object-Remote-tests.list

%changelog

%autochangelog
