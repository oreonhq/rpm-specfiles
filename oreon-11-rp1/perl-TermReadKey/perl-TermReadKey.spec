Name:           perl-TermReadKey
Version:        2.38
Release:        27%{?dist}
Summary:        A perl module for simple terminal control
License:        TermReadKey AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/TermReadKey
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.gz
Patch0: perl-TermReadKey-configure-c99.patch
# oreon url source checksums begin
%global source0_sha256 5a645878dc570ac33661581fbb090ff24ebce17d43ea53fd22e105a856a47290
%global source0_file TermReadKey-2.38.tar.gz
# oreon url source checksums end
# Build
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Term::ReadKey is a compiled perl module dedicated to providing simple
control over terminal driver modes (cbreak, raw, cooked, etc.)
support for non-blocking reads, if the architecture allows, and some
generalized handy functions for working with terminals.  One of the
main goals is to have the functions as portable as possible, so you
can just plug in "use Term::ReadKey" on any architecture and have a
good likelyhood of it working.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/TermReadKey-2.38.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5a645878dc570ac33661581fbb090ff24ebce17d43ea53fd22e105a856a47290" || { echo "oreon: Source0 SHA256 mismatch for TermReadKey-2.38.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n TermReadKey-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build} OPTIMIZE="%{optflags}"

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
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
make test

%files
%doc Changes example README
%{perl_vendorarch}/Term*
%{perl_vendorarch}/auto/Term*
%{_mandir}/man3/Term::ReadKey*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.38-27
- Prepare for Oreon 11 (RP1)
