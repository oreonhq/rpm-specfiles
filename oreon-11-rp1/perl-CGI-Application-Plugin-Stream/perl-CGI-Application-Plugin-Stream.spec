%global source0_hash 2c1606dd044805dc403f245022992ca88600f833bee2ce834a9046b6b4b119b1

Name:           perl-CGI-Application-Plugin-Stream
Version:        2.12
Release:        32%{?dist}
Summary:        CGI::Application Plugin for streaming files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-Stream
Source0:        https://cpan.metacpan.org/authors/id/P/PU/PURDY/CGI-Application-Plugin-Stream-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application) >= 3.21
BuildRequires:  perl(File::MMagic)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
This plugin provides a way to stream a file back to the user, which is
useful if you are creating a PDF or Spreadsheet document dynamically to
deliver to the user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-Stream-%{version}

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
