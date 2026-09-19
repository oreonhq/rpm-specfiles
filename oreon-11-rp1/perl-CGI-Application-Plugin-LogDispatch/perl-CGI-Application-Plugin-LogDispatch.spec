%global source0_hash f71008b327464d096440bff646c9cf37def221f74598545388572742548486ed

Name:           perl-CGI-Application-Plugin-LogDispatch
Version:        1.02
Release:        48%{?dist}
Summary:        Add Log::Dispatch support to CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-LogDispatch
Source0:        https://cpan.metacpan.org/authors/id/C/CE/CEESHEK/CGI-Application-Plugin-LogDispatch-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Log::Dispatch) >= 0.21
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Sub::WrapPackages)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(Sub::WrapPackages)

%{?perl_default_filter}

%description
CGI::Application::Plugin::LogDispatch adds logging support to your
CGI::Application modules by providing a Log::Dispatch dispatcher object
that is accessible from anywhere in the application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-LogDispatch-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
