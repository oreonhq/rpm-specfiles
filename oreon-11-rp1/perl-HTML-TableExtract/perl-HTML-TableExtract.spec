%global source0_hash 86c59c9d58da3ca174da5e62f5a0fb02f4da02b1b1e01df9e5d14bb65e4c3ecf
Name:           perl-HTML-TableExtract
Version:        2.15
Release:        1%{?dist}
Summary:        A Perl module for extracting content in HTML tables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://www.mojotoad.com/sisk/projects/HTML-TableExtract/
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSISK/HTML-TableExtract-%{version}.tar.gz
Patch0:         HTML-TableExtract-2.15-fix-testsuite.patch
BuildArch:      noarch
Requires:       perl(HTML::ElementTable) >= 1.16
Requires:       perl(HTML::TreeBuilder)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::ElementTable)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HTML::TableExtract is a module that simplifies the extraction of
information contained in tables within HTML documents.

Tables of note may be specified using Headers, Depth, Count,
Attributes, or some combination of the three. See the module
documentation for details.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-TableExtract-%{version} 
%patch -P0 -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

HTE_DEV_TESTS=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
