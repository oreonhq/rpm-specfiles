Name:           perl-Term-Cap
Version:        1.18
Release:        521%{?dist}
Summary:        Perl termcap interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Cap
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSTOWE/Term-Cap-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 7d5b155824223b4c5cc2587b9dea15f7a5c8f7fd9eaf704a9a6828557a527d0a
%global source0_file Term-Cap-1.18.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
# ncurses for infocmp tool
BuildRequires:  ncurses
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)
# ncurses for infocmp tool
Requires:       ncurses
Requires:       perl(Carp)
Conflicts:      perl < 4:5.22.0-347

%description
These are low-level functions to extract and use capabilities from a terminal
capability (termcap) database.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Term-Cap-1.18.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7d5b155824223b4c5cc2587b9dea15f7a5c8f7fd9eaf704a9a6828557a527d0a" || { echo "oreon: Source0 SHA256 mismatch for Term-Cap-1.18.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Term-Cap-%{version}
# Help generators to recognize Perl scripts
perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' test.pl
chmod +x test.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a test.pl %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . test.pl
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Term*
%{_mandir}/man3/Term::Cap*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.18-521
- Prepare for Oreon 11 (RP1)
