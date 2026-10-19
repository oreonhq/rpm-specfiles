%global source0_hash f350069f31db2dab65b68a1d4a1bdb854ece8b91f8bd43bf822b828151708f47
Name:           perl-CGI-Application-Plugin-Forward
Version:        1.06
Release:        47%{?dist}
Summary:        Pass control from one run mode to another in CGI::Application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-Forward
Source0:        https://cpan.metacpan.org/authors/id/M/MG/MGRAHAM/CGI-Application-Plugin-Forward-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::Application::Plugin::AutoRunmode)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module gives CGI::Application a forward method that passes control
to another run mode and returns its output. This is equivalent to calling
$self->$other_runmode, except that CGI::Application's internal value of
the current run mode is updated.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-Forward-%{version}

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
