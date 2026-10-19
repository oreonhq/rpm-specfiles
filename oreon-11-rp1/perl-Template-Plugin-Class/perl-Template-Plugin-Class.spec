%global source0_hash 0604fe8ae7bf3ad9679e64d9b1ad4c9e9014c177aa80e835d52a86f78d9707c3
Name:           perl-Template-Plugin-Class
Version:        0.14
Release:        46%{?dist}
Summary:        Allow calling of class methods on arbitrary classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Plugin-Class
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Template-Plugin-Class-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Template::Plugin)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Template::Plugin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
