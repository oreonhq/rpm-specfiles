Name:           perl-CGI
Summary:        Handle Common Gateway Interface requests and responses
Version:        4.71
Release:        2%{?dist}
License:        Artistic-2.0
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-%{version}.tar.gz
URL:            https://metacpan.org/release/CGI
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-requires:
BuildRequires:  perl(Carp)
# Config not needed on Linux
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(File::Temp) >= 0.17
BuildRequires:  perl(HTML::Entities) >= 3.69
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
# Text::ParseWords not used at tests
BuildRequires:  perl(URI) >= 1.76
BuildRequires:  perl(warnings)
# Apache modules are optional
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Warn) >= 0.3
BuildRequires:  perl(utf8)
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(File::Temp) >= 0.17
Requires:       perl(HTML::Entities) >= 3.69
Requires:       perl(Text::ParseWords)
Requires:       perl(URI) >= 1.76

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec)\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Temp)\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((URI)\\)$
# Remove false dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Fh)\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MultipartBuffer\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Fh\\)

# Filter modules bundled for tests
%global __requires_exclude %{__requires_exclude}|^perl\\(Apache)\s*$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

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
# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
rm %{buildroot}/%{_libexecdir}/%{name}/t/compiles_pod.t
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README.md examples/
%{perl_vendorlib}/CGI*
%{perl_vendorlib}/Fh*
%{_mandir}/man3/CGI*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.71-2
- Prepare for Oreon 11 (RP1)
