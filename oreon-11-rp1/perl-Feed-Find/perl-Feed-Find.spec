%global source0_hash 39143f7e28ec3866fb124144a8c8d37ba6279029e9d33b521a00620ddfad8d07
Name:           perl-Feed-Find
Version:        0.13
Release:        1%{?dist}
Summary:        Syndication feed auto-discovery
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Feed-Find
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/Feed-Find-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(Config)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::Include)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Feed::Find implements feed auto-discovery for finding syndication feeds, 
given a URI. It (currently) passes all of the auto-discovery tests at 
http://diveintomark.org/tests/client/autodiscovery/.

Feed::Find will discover the following feed formats:

    * RSS 0.91
    * RSS 1.0
    * RSS 2.0
    * Atom

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Feed-Find-%{version}

# Remove bundled libraries
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
find -type f -exec chmod -x {} +

# Help file to recognise the Perl scripts
for F in t/*.t t/data/autodiscover/*; do
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
%files -n perl-Feed-Find-tests -f %{oreon_filedir}/perl-Feed-Find-tests.list

%changelog

%autochangelog
