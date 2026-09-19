%global source0_hash 9286ac034ecc666d52de5de621bbeb8e3cb052b23c076e544c2cc346edf6ca27

Name:           perl-CGI-Application-Plugin-FormState
Version:        0.12
Release:        45%{?dist}
Summary:        Store Form State without Hidden Fields
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-FormState
Source0:        https://cpan.metacpan.org/authors/id/M/MG/MGRAHAM/CGI-Application-Plugin-FormState-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::Application::Plugin::Session)
BuildRequires:  perl(CGI::Session)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
CGI::Application::Plugin::FormState provides a temporary storage area
within the user's session for storing form-related data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-FormState-%{version}

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
