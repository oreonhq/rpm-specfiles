%global source0_hash a6b69bac79a253003446b283efa6f3aeffa609d0c1c52b4209878212da70f9ab
Name:           perl-CPAN-02Packages-Search
Version:        0.100
Release:        7%{?dist}
Summary:        Search Perl modules in 02packages.details.txt
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-02Packages-Search
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/CPAN-02Packages-Search-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Search::Dict) >= 1.07
Requires:       perl(Tie::Handle::SkipHeader) >= 0.004
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude|}}^perl\\((Search::Dict|Tie::Handle::SkipHeader)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Search::Dict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Handle::SkipHeader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
CPAN::02Packages::Search allows you to search Perl modules in the de facto
standard CPAN index file 02packages.details.txt.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPAN-02Packages-Search-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
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
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-CPAN-02Packages-Search-tests -f %{oreon_filedir}/perl-CPAN-02Packages-Search-tests.list

%changelog

%autochangelog
