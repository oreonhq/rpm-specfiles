%global source0_hash de5c1c257fd19e54c21e36fac87aaeb57a2993e9e796500fab41b93e76199717
Name:       perl-Term-Completion 
Version:    1.02
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Read one line of user input, with convenience functions
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Term-Completion-%{version}.tar.gz
Url:        https://metacpan.org/release/Term-Completion
BuildArch:  noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::Size)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Term::Completion is an extensible, highly configurable replacement for
the venerable Term::Complete package. It is object-oriented and thus allows
subclassing. Two derived classes are Term::Completion::Multi and 
Term::Completion::Path. A prompt is printed and the user may enter one line
of input, submitting the answer by pressing the ENTER key. 

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(IO::String)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-Completion-%{version}
find . -type f -exec chmod -c -x {} \;
perl -pi -e 's|^#!/opt/perl_5.8.8/bin/perl|#!%{__perl}|' devel/tget.pl
for file in README.md Changes devel/*; do
    perl -pi -e 's/\r//g' ${file}
done

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
rm %{buildroot}%{_libexecdir}/%{name}/t/08_path.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
export COLUMNS=80
export LINES=25
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export COLUMNS=80
export LINES=25
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Term-Completion-tests -f %{oreon_filedir}/perl-Term-Completion-tests.list

%changelog

%autochangelog
