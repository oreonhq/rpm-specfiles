%global source0_hash 709a7dc4a2259683eb2f89e085ec70cf743710d950510e489ec6ddca3eb80c68
Name:           perl-podlators
Epoch:          1
Version:        6.1.1
Release:        1%{?dist}
Summary:        Format POD source into various output formats
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND FSFAP
URL:            https://metacpan.org/release/podlators
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRA/podlators-v%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Basename)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(PerlIO)
Requires:       perl(Pod::Simple) >= 3.26
Conflicts:      perl < 4:5.16.1-234
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::Simple\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Podlators\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::RRA.*\\)
Provides:       perl(Pod::Man)
Provides:       perl(Pod::Text)
Provides:       perl(Pod::Text::Color)
Provides:       perl(Pod::Text::Termcap)
Provides:       perl(Pod::ParseLink)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::Cap)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(autodie)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package contains Pod::Man and Pod::Text modules which convert POD input
to *roff source output, suitable for man pages, or plain text.  It also
includes several sub-classes of Pod::Text for formatted output to terminals
with various capabilities.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(PerlIO)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n podlators-v%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
for F in `find %{buildroot}%{_libexecdir}/%{name} -name *.t -o -name *.pm`; do
    perl -i -pe "s{'t', 'tmp'}{'/tmp'}" $F
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING AUTOMATED_TESTING RELEASE_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
unset AUTHOR_TESTING AUTOMATED_TESTING RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-podlators-tests -f %{oreon_filedir}/perl-podlators-tests.list

%changelog

%autochangelog
