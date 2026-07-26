%global source0_hash f7ff7e369d8293a394cb3783b54b745e7faf44422e8a83bfcc359378a6e56145

# Enable Excel file format support
%bcond_without perl_SQL_Translator_enables_excel

Name:           perl-SQL-Translator
Summary:        Manipulate structured data definitions (SQL and more)
Version:        1.66
Release:        4%{?dist}
# script/sqlt*: GPL-2.0-only
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND GPL-2.0-only
Source0:        https://cpan.metacpan.org/authors/id/V/VE/VEESH/SQL-Translator-%{version}.tar.gz
URL:            https://metacpan.org/release/SQL-Translator
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Pretty)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI) >= 1.54
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir) >= 1.0
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(GD)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Graph::Directed)
BuildRequires:  perl(GraphViz)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moo) >= 1.000003
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(overload)
BuildRequires:  perl(Package::Variant) >= 1.001001
BuildRequires:  perl(Parse::RecDescent) >= 1.967009
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
%if %{with perl_SQL_Translator_enables_excel}
BuildRequires:  perl(Spreadsheet::ParseExcel) >= 0.41
%endif
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Template) >= 2.20
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::RecordParser) >= 0.02
BuildRequires:  perl(Try::Tiny) >= 0.04
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::LibXML) >= 1.69
BuildRequires:  perl(XML::LibXML::XPathContext)
BuildRequires:  perl(XML::Writer) >= 0.500
BuildRequires:  perl(YAML) >= 0.66
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception) >= 0.42
BuildRequires:  perl(XML::Parser)
# Optional tests:
# DBD::Pg not needed because it requires preconfigures PostgreSQL database
# with DBICTEST_PG_* environemnt variables
# Test::PostgreSQL not yet packaged
# xt/* tests are not run
#BuildRequires:  perl(Test::EOL) >= 1.1
#BuildRequires:  perl(Test::NoTabs) >= 1.1
#BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::PostgreSQL)
Requires:       perl(CGI)
Requires:       perl(CGI::Pretty)
Requires:       perl(DBI) >= 1.54
Requires:       perl(File::ShareDir) >= 1.0
Requires:       perl(Graph::Directed)
Requires:       perl(JSON::MaybeXS) >= 1.003003
Requires:       perl(overload)
Requires:       perl(Package::Variant) >= 1.001001
Requires:       perl(Parse::RecDescent) >= 1.967009
%if %{with perl_SQL_Translator_enables_excel}
Requires:       perl(Spreadsheet::ParseExcel) >= 0.41
%endif
Requires:       perl(Template) >= 2.20
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Text::RecordParser) >= 0.02
Requires:       perl(Try::Tiny) >= 0.04
Requires:       perl(XML::LibXML) >= 1.69
Requires:       perl(XML::Writer) >= 0.500

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((DBI|File::ShareDir|JSON::MaybeXS|Moo|Package::Variant|Parse::RecDescent|Spreadsheet::ParseExcel|Template|Test::More|Text::RecordParser|Try::Tiny|XML::LibXML)\\)$
# Remove badly detected requires (a grammar in the
# lib/SQL/Translator/Parser/Sybase.pm)
%global __requires_exclude %{__requires_exclude}|^perl\\(:\\)
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
SQL::Translator is a group of Perl modules that converts vendor-specific
SQL table definitions into other formats, such as other vendor-specific
SQL, ER diagrams, documentation (POD and HTML), XML, and Class::DBI
classes.  The main focus of SQL::Translator is SQL, but parsers exist
for other structured data formats%{?with_perl_SQL_Translator_enables_excel:, including Excel spreadsheets} and
arbitrarily delimited text files.  Through the separation of the code into
parsers and producers with an object model in between, it’s possible to
combine any parser with any producer, to plug in custom parsers or
producers, or to manipulate the parsed data via the built-in object model.
Presently only the definition parts of SQL are handled (CREATE, ALTER),
not the manipulation of data (INSERT, UPDATE, DELETE).

%package Producer-Diagram
Summary:        ER diagram producer for SQL::Translator

%description Producer-Diagram
ER diagram producer for SQL::Translator.

%package Producer-GraphViz
Summary:        GraphViz diagram producer for SQL::Translator

%description Producer-GraphViz
GraphViz diagram producer for SQL::Translator.

%package -n sqlt-graph
Summary:        sqlt-graph tool to create a graph from a database schema
License:        GPL-2.0-only
Obsoletes:      %{name} < 1.62-4

%description -n sqlt-graph
The sqlt-graph tool from %{name} that can automatically create a graph
from a database schema. Packaged separately to avoid the main package
depending on Graphviz.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Producer-Diagram = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Producer-GraphViz = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       sqlt-graph = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBD::SQLite)
Requires:       perl(XML::Parser)
Requires:       perl(Test::PostgreSQL)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-Translator-%{version}
# Fix shell-bangs
perl -MConfig -pi -e 's|^#!.*perl\b|$Config{startperl}|' script/*
# Fix permission, CPAN RT#100532
chmod -x lib/SQL/Translator/Parser/JSON.pm
%if %{without perl_SQL_Translator_enables_excel}
# Remove Excel support
rm lib/SQL/Translator/Parser/Excel.pm
perl -i -ne 'print $_ unless m{^lib/SQL/Translator/Parser/Excel\.pm}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/script
for F in sqlt sqlt.cgi sqlt-diagram sqlt-diff sqlt-diff-old sqlt-dumper sqlt-graph; do
    ln -s %{_bindir}/$F %{buildroot}%{_libexecdir}/%{name}/script
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{_bindir}/sqlt*
%dir %{perl_vendorlib}/SQL
%{perl_vendorlib}/SQL/Translator*
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/SQL
%{perl_vendorlib}/auto
%{_mandir}/man1/sqlt*
%{_mandir}/man3/SQL::Translator*
%{_mandir}/man3/Test::SQL::Translator*
%exclude %{perl_vendorlib}/SQL/Translator/Producer/Diagram.pm
%exclude %{perl_vendorlib}/SQL/Translator/Producer/GraphViz.pm
%exclude %{_mandir}/man1/sqlt-graph.*
%exclude %{_mandir}/man3/SQL::Translator::Producer::Diagram.*
%exclude %{_mandir}/man3/SQL::Translator::Producer::GraphViz.*
%exclude %{_bindir}/sqlt-graph

%files Producer-Diagram
%{perl_vendorlib}/SQL/Translator/Producer/Diagram.pm
%{_mandir}/man3/SQL::Translator::Producer::Diagram.*

%files Producer-GraphViz
%{perl_vendorlib}/SQL/Translator/Producer/GraphViz.pm
%{_mandir}/man3/SQL::Translator::Producer::GraphViz.*

%files -n sqlt-graph
%{_bindir}/sqlt-graph
%{_mandir}/man1/sqlt-graph.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
