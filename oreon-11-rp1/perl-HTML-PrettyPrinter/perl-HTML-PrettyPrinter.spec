%global source0_hash 1bda2edf2cdda3c9a97cfd55ab2792f7254202b7b56b51ebaecea54ac46edab6
Name:           perl-HTML-PrettyPrinter
Version:        0.03
Release:        51%{?dist}
Summary:        Generate nice HTML files from HTML syntax trees
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-PrettyPrinter
Source0:        https://cpan.metacpan.org/authors/id/C/CL/CLMS/HTML-PrettyPrinter-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Element)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(Test)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HTML::PrettyPrinter produces nicely formatted HTML code from a HTML syntax
tree. It is especially useful if the produced HTML file shall be read or
edited manually afterwards. Various parameters let you adapt the output to
different styles and requirements.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-PrettyPrinter-%{version}
iconv -f iso8859-1 -t utf-8 PrettyPrinter.pm > PrettyPrinter.pm.conv \
&& mv -f PrettyPrinter.pm.conv PrettyPrinter.pm 

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
