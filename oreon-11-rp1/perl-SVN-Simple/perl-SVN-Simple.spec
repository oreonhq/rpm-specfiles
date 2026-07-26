%global source0_hash d63cc169e4369be98a539abe9cc1611bfcc2b36966a6517e676688fed1884ffb

Name:           perl-SVN-Simple
Version:        0.28
Release:        40%{?dist}
Summary:        A simple interface for writing a delta editor
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SVN-Simple
Source0:        https://cpan.metacpan.org/modules/by-module/SVN/SVN-Simple-%{version}.tar.gz
# Retrieved from upstream bugtracker:
# http://rt.cpan.org/Ticket/Attachment/716566/369865/deep.diff
# http://rt.cpan.org/Public/Bug/Display.html?id=51087
Patch0:         perl-SVN-Simple-test.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(SVN::Core)

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

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
