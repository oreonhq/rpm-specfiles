%global source0_hash a781722b9626e63f5dc74a3666291ed0995c05416f7505aab6ce084a8687e620
Name:           perl-CGI-Application-Plugin-CAPTCHA
Version:        0.04
Release:        1%{?dist}
Summary:        Easily create, use, and verify CAPTCHAs in CGI::Application-based web apps
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-CAPTCHA
Source0:        https://cpan.metacpan.org/authors/id/C/CR/CROMEDOME/CGI-Application-Plugin-CAPTCHA-%{version}.tar.gz
Patch0:         CGI-Application-Plugin-CAPTCHA-0.04-Wait-until-test-server-can-accept-connections.patch
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Data::Random)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(GD::SecurityImage)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::WWW::Mechanize)
BuildRequires:  perl-generators
# /oreon:deps
%description
CGI::Application::Plugin::CAPTCHA allows programmers to easily add and
verify CAPTCHAs in their CGI::Application-derived web applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-CAPTCHA-%{version}
%patch -P0 -p1

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
