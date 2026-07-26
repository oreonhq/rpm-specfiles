%global source0_hash 0604fe8ae7bf3ad9679e64d9b1ad4c9e9014c177aa80e835d52a86f78d9707c3

Name:           perl-Template-Plugin-Class
Version:        0.14
Release:        46%{?dist}
Summary:        Allow calling of class methods on arbitrary classes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Plugin-Class
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Template-Plugin-Class-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Template::Plugin), perl(Module::Build), perl(Test::More)
Requires:       perl(Template::Plugin)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Plugin-Class-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/Template/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
