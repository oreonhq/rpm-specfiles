%global source0_hash ababf6d81c079a921cbbc5a2ff1bc58f8ff5edb47b08c6b9f6aaf3bf4db2624e

Name:           perl-App-SVN-Bisect
Version:        1.1
Release:        42%{?dist}
Summary:        Binary search through svn revisions
License:        Artistic-2.0
URL:            https://metacpan.org/release/App-SVN-Bisect
Source0:        https://cpan.metacpan.org/modules/by-module/App/INFINOID/App-SVN-Bisect-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  subversion
Requires:       subversion

%description
This module implements the backend of the "svn-bisect" command line tool.
See the POD documentation of that tool, for usage details.

%package -n svn-bisect
License: Artistic-2.0
Summary: Binary search through svn revisions
Requires: %{name} = 0:%{version}-%{release} 

%description -n svn-bisect
This is a command-line tool inspired by "git-bisect", which allows you to
perform binary searches among the revisions of a subversion project.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-SVN-Bisect-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes LICENSE README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files -n svn-bisect
%doc Changes LICENSE README TODO
%{_bindir}/svn-bisect
%{_mandir}/man1/svn-bisect.1*

%changelog
%autochangelog
