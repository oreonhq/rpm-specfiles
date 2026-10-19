%global source0_hash d63cc169e4369be98a539abe9cc1611bfcc2b36966a6517e676688fed1884ffb
Name:           perl-SVN-Simple
Version:        0.28
Release:        1%{?dist}
Summary:        A simple interface for writing a delta editor
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SVN-Simple
Source0:        https://cpan.metacpan.org/modules/by-module/SVN/SVN-Simple-%{version}.tar.gz
Patch0:         perl-SVN-Simple-test.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(SVN::Core)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
%description 
SVN::Simple::Edit wraps the subversion delta editor with
a perl friendly interface and then you could easily drive it for
describing changes to a tree. A common usage is to wrap the commit
editor, so you could make commits to a subversion repository easily.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SVN-Simple-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;
chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
