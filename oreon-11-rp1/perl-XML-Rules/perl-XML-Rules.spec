%global source0_hash 3788255c07afe4195a0de72ce050652320d817528ff2d10c611f6e392043868b
Name:		perl-XML-Rules
Version:	1.16
Release:        1%{?dist}
Summary:        Parse XML and specify what and how to keep/process for individual tags
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/XML-Rules
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-Rules-%{version}.tar.gz
Patch0:		XML-Rules-1.10-add-shebang.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Parser::Expat)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
