%global source0_hash 183bde1ae7aba70dcb3ed777c5548237f42c3ed551fd5bc658cee86d0216acb1
Name:           perl-Test-WWW-Mechanize-Catalyst
Summary:        Test::WWW::Mechanize for Catalyst
Version:        0.62
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/Test-WWW-Mechanize-Catalyst-%{version}.tar.gz
URL:            https://metacpan.org/release/Test-WWW-Mechanize-Catalyst
BuildArch:      noarch
%if !0%{?perl_bootstrap}
%endif
Requires:       perl(Catalyst) >= 5.00
Requires:       perl(LWP) >= 5.816
Requires:       perl(Moose) >= 0.67
Requires:       perl(namespace::clean) >= 0.09
Requires:       perl(Test::WWW::Mechanize) >= 1.14
Requires:       perl(WWW::Mechanize) >= 1.54
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::Dummy)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::WWW::Mechanize)
BuildRequires:  perl(Test::utf8)
BuildRequires:  perl(URI)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Catalyst is an elegant MVC Web Application Framework. Test::WWW::Mechanize
is a subclass of WWW::Mechanize that incorporates features for web
application testing. The Test::WWW::Mechanize::Catalyst module meshes the
two to allow easy testing of Catalyst applications without starting up a
web server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-WWW-Mechanize-Catalyst-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

# silence rpmlint warning
sed -i '1s,#!.*perl,#!%{__perl},' t/*.t

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
