%global source0_hash 7e30ef4cc73b32e426c4360dcd104e8f9af6de45d865b42952fe5c7a15c7a150

Name:           perl-Apache-Session-Wrapper
Version:        0.34
Release:        43%{?dist}
Summary:        A simple wrapper around Apache::Session
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Apache-Session-Wrapper
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/Apache-Session-Wrapper-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:	perl-generators
BuildRequires:	perl(Apache2::Cookie), perl(Apache::Session), perl(Class::Container), perl(Exception::Class)
BuildRequires:	perl(Params::Validate), perl(Module::Build), perl(Test::Pod)
Requires:	perl(Class::Container)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-Session-Wrapper-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
APACHE_TEST_HTTPD=/usr/sbin/httpd ./Build test

%files
%doc Changes LICENSE
%{perl_vendorlib}/Apache/Session/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
