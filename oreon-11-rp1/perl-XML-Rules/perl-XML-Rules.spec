%global source0_hash 3788255c07afe4195a0de72ce050652320d817528ff2d10c611f6e392043868b

Name:		perl-XML-Rules
Version:	1.16
Release:	39%{?dist}
Summary:	Parse XML and specify what and how to keep/process for individual tags
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/XML-Rules
Source0:	https://cpan.metacpan.org/modules/by-module/XML/XML-Rules-%{version}.tar.gz
Patch0:		XML-Rules-1.10-add-shebang.patch
BuildArch:	noarch

# build requirements
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build)
BuildRequires:	sed

# module requirements
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XML::Parser) >= 2.00
BuildRequires:	perl(XML::Parser::Expat) >= 2.00

# test requirements
BuildRequires:	perl(Encode)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(utf8)

# optional tests
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04

# dependencies
# (none)

%description
The XML::Rules module provides an API layer on top of XML::Parser.  It
allows you to specify rules that are subroutines to be run once a tag
is fully parsed and either process the data from the tag itself and
its children or specify what parts of the data and how to add to the
data structure being built for the parent tag.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Rules-%{version}

# fix end of line encoding
find . -type f -exec sed -i 's/\r//' {} \;

# the patch assumes the end of lines have already been fixed
%patch -P0 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README example
%license LICENSE
%{_bindir}/dtd2XMLRules.pl
%{_bindir}/xml2XMLRules.pl
%{perl_vendorlib}/XML/
%{_mandir}/man3/XML::Rules.3*

%changelog
%autochangelog
