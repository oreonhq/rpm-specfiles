%global source0_hash 2bda042f2aa4d7bd714b772c58a3948dc4afbc1017536b64d31b90d161122a16

Name:           perl-Dist-Zilla-Plugin-ReadmeFromPod
Version:        0.40
Release:        3%{?dist}
Summary:        Automatically convert POD to a README for Dist::Zilla
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-ReadmeFromPod
Source0:        https://cpan.metacpan.org/authors/id/F/FA/FAYLAND/Dist-Zilla-Plugin-ReadmeFromPod-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
# glibc-coreutils for iconv tool
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Dist::Zilla::File::InMemory not used at tests
# Dist::Zilla::Role::FilePruner version from Dist::Zilla in META
BuildRequires:  perl(Dist::Zilla::Role::FilePruner) >= 6.000
BuildRequires:  perl(Dist::Zilla::Role::InstallTool) >= 5
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moose)
BuildRequires:  perl(Path::Tiny) >= 0.004
BuildRequires:  perl(Pod::Readme) >= 1.2.0
# Tests:
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       perl(Dist::Zilla::File::InMemory)
# Dist::Zilla::Role::FilePruner version from Dist::Zilla in META
Requires:       perl(Dist::Zilla::Role::FilePruner) >= 6.000
Requires:       perl(Dist::Zilla::Role::InstallTool) >= 5
Requires:       perl(Pod::Readme) >= 1.2.0
# Module names passed to Module::Load::load() via Pod::Readme::new() from %%FORMAT
Recommends:     perl(Pod::Markdown)
Recommends:     perl(Pod::Markdown::Github)
Recommends:     perl(Pod::Simple::HTML)
Recommends:     perl(Pod::Simple::RTF)
Recommends:     perl(Pod::Simple::Text)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::Readme\\)$

%description
Generate the README file from main_module (or other if specified)
with Pod::Readme.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-ReadmeFromPod-%{version}
# Normalize encoding
iconv -f ISO-8859-1 -t UTF-8 < README.md > README.md.utf8
touch -r README.md README.md.utf8
mv README.md.utf8 README.md
# Remove always skipped tests
for F in t/author-pod-syntax.t t/release-kwalitee.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README.md
%dir %{perl_vendorlib}/Dist
%dir %{perl_vendorlib}/Dist/Zilla
%dir %{perl_vendorlib}/Dist/Zilla/Plugin
%{perl_vendorlib}/Dist/Zilla/Plugin/ReadmeFromPod.pm
%{_mandir}/man3/Dist::Zilla::Plugin::ReadmeFromPod.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
