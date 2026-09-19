%global source0_hash df7dd1167794252fd4bb4aad1ae487aa1dc96109d5d19a7f6cdea42c39c50f70

Name:           perl-Dist-Zilla-Plugin-GithubMeta
Version:        0.58
Release:        25%{?dist}
Summary:        Automatically include GitHub meta information in META.yml
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-GithubMeta
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Dist-Zilla-Plugin-GithubMeta-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types::URI)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(version)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More)

%description
Dist::Zilla::Plugin::GithubMeta is a Dist::Zilla plugin to include
GitHub meta information in META.yml.  It automatically detects if the
distribution directory is under git version control and whether the
origin is a GitHub repository and will set the repository and homepage
meta in META.yml to the appropriate URLs for GitHub.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-GithubMeta-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/00*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/author-*
cp -a corpus %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
