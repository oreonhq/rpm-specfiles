%global source0_hash c7474050be80201f1fb55f0a569b9c0ab6c1c3f0cebbd7e601bda9b4046eec85

Name:           perl-Template-Toolkit
Version:        3.106
Release:        1%{?dist}
Summary:        Template processing system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://www.template-toolkit.org/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/Template-Toolkit-%{version}.tar.gz
# No 225 version available
Source1:        http://tt2.org/download/TT_v224_html_docs.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AppConfig)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time:
# Not used for tests - perl(Apache::Util)
BuildRequires:  perl(base)
BuildRequires:  perl(CGI) >= 4.11
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::Entities)
# Prefer Image::Info over Image::Size
BuildRequires:  perl(Image::Info)
BuildRequires:  perl(locale)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Text::Wrap)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdArray)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(utf8)
# Apache::Util pulls in mod_perl and httpd, for cmd-line tools using
# Template-Toolkit this is a lot of unnecessary and often unwanted packages
# The code checks for the existence of either Apache::Util or HTML::Entities,
# and the latter is much lighter weight from a dependency footprint.
# https://bugzilla.redhat.com/show_bug.cgi?id=1802358
# Requires:     perl(Apache::Util)
Requires:       perl(Encode)
Requires:       perl(File::Temp)
Requires:       perl(HTML::Entities)
# Prefer Image::Info over Image::Size
Requires:       perl(Image::Info)
Requires:       perl(Math::Trig)
Provides:       perl-Template-Toolkit-examples = %{version}-%{release}
Obsoletes:      perl-Template-Toolkit-examples < 2.22-1

%global __provides_exclude ^perl\\(bytes\\)
%{?perl_default_filter}


Provides:       perl(Template)
Provides:       perl(Template::Toolkit)
%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system.
It was originally designed and remains primarily useful for generating
dynamic web content, but it can be used equally well for processing
any other kind of text based documents: HTML, XML, POD, PostScript,
LaTeX, and so on.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Template-Toolkit-%{version} -a 1
find lib -type f | xargs chmod -c -x
find TT_v*_html_docs -depth -name .svn -type d -exec rm -rf {} \;
find TT_v*_html_docs -type f -exec chmod -x {} +;

# Convert file to UTF-8
iconv -f iso-8859-1 -t utf-8 -o Changes{.utf8,}
mv Changes{.utf8,}


%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor \
  TT_DBI=n TT_ACCEPT=y NO_PERLLOCAL=1 NO_PACKLIST=1
%make_build OPTIMIZE="%{optflags}"


%install
%make_install \
  TT_PREFIX=%{buildroot}%{_datadir}/tt2
chmod -R u+w %{buildroot}/*
# Nuke buildroot where it hides
sed -i "s|%{buildroot}||g" %{buildroot}%{perl_vendorarch}/Template/Config.pm


%check
make test


%files
%doc AI_POLICY.md Changes README.md SECURITY.md TODO
%doc TT_v*_html_docs/*
%{_bindir}/tpage
%{_bindir}/ttree
%{perl_vendorarch}/Template.pm
%{perl_vendorarch}/auto/Template
%{perl_vendorarch}/Template
%{_mandir}/man1/tpage.1*
%{_mandir}/man1/ttree.1*
%{_mandir}/man3/Template*.3*


%changelog
%autochangelog
