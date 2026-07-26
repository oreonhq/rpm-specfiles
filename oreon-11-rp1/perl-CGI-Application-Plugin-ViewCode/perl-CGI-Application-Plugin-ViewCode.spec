%global source0_hash 15fa6b23e1679ec7e5b8d86daa48a40134f038dbe2ab68bdbc34b0293e434d46

Name:           perl-CGI-Application-Plugin-ViewCode
Version:        1.02
Release:        49%{?dist}
Summary:        Allows you to view the source of a CGI::Application module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-ViewCode
Source0:        https://cpan.metacpan.org/authors/id/W/WO/WONKO/CGI-Application-Plugin-ViewCode-%{version}.tar.gz
# Perl 5.18 compatibility, CPAN RT#73317
Patch0:         CGI-Application-Plugin-ViewCode-1.02-qw-does-not-produce-parentheses-anymore.patch

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Xhtml)
BuildRequires:  perl(Syntax::Highlight::Perl::Improved)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
This plugin works by adding extra run modes (named view_code and view_pod)
to the application. By calling this run mode you can see the source or POD
of the running module (by default) or you can specify which module you
would like to view.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-ViewCode-%{version}
%patch -P0 -p1

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
