%global source0_hash c191c6d5eceb8cb75c0565192360662d202d716bad07a233c4b329a4284dc71b

Name:           perl-Text-Markdown
Version:        1.000031
Release:        35%{?dist}
Summary:        Convert Markdown syntax to (X)HTML

License:        BSD-3-Clause
URL:            https://metacpan.org/release/Text-Markdown
Source0:        https://cpan.metacpan.org/modules/by-module/Text/Text-Markdown-%{version}.tar.gz
# Fix building on Perl without "." in @INC,
# <https://github.com/bobtfish/text-markdown/issues/41>
Patch0:         Text-Markdown-1.000031-Unbundle-inc-Module-Install.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
# perl-podlators for pod2text
BuildRequires:  perl-podlators
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
%if 0%{fedora} < 36
BuildRequires:  perl(HTML::Tidy)
%endif
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Text::Balanced)
# Text::Diff not helpful
BuildRequires:  perl(warnings)
BuildRequires:  sed

%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format
is most similar to that of plain text email, and supports features
such as headers, *emphasis*, code blocks, blockquotes, and links.

Markdown's syntax is designed not as a generic markup language, but
specifically to serve as a front-end to (X)HTML. You can use
span-level HTML tags anywhere in a Markdown document, and you can use
block level HTML tags (like <div> and <table> as well).

For more information about Markdown's syntax, see:

    http://daringfireball.net/projects/markdown/

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Markdown-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm %{buildroot}%{_libexecdir}/%{name}/t/02pod.t %{buildroot}%{_libexecdir}/%{name}/t/03podcoverage.t
# Switch tests to use Markdown.pl in system
sed -i 's/\$Bin\/\.\.\/script\/Markdown\.pl/\/usr\/bin\/Markdown.pl/' %{buildroot}%{_libexecdir}/%{name}/t/34commandlinemarkdown.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%license License.text
%doc Changes README Readme.text Todo
# For noarch packages: vendorlib
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/Markdown.pl

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
