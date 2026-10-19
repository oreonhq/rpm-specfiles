%global source0_hash babc1ca72db188083a1c3812debe88c4473b943b1f7c662281cd57c580a8bdd9
Name:           perl-CGI
Summary:        Handle Common Gateway Interface requests and responses
Version:        4.72
Release:        1%{?dist}
License:        Artistic-2.0
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-%{version}.tar.gz
URL:            https://metacpan.org/release/CGI
BuildArch:      noarch
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(File::Temp) >= 0.17
Requires:       perl(HTML::Entities) >= 3.69
Requires:       perl(Text::ParseWords)
Requires:       perl(URI) >= 1.76
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec)\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Temp)\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((URI)\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Fh)\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MultipartBuffer\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Fh\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Apache)\s*$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
Provides:       perl(CGI)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(URI)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
CGI.pm is a stable, complete and mature solution for processing and preparing
HTTP requests and responses. Major features including processing form
submissions, file uploads, reading and writing cookies, query string
generation and manipulation, and processing and preparing HTTP headers. Some
HTML generation utilities are included as well.

CGI.pm performs very well in in a vanilla CGI.pm environment and also comes 
with built-in support for mod_perl and mod_perl2 as well as FastCGI.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n CGI-%{version}
iconv -f iso8859-1 -t utf-8 < Changes > Changes.1
mv Changes.1 Changes
chmod -c -x examples/*

# Help file to recognise the Perl scripts
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
rm %{buildroot}/%{_libexecdir}/%{name}/t/compiles_pod.t
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-CGI-tests -f %{oreon_filedir}/perl-CGI-tests.list

%changelog

%autochangelog
