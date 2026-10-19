%global source0_hash e43cd995ad9157a7e839d993ee7b6c4d1854947e557d096d9d5aaf74507fab33
Name:           perl-Text-WikiFormat
Version:        0.81
Release:        32%{?dist}
Summary:        Translate Wiki formatted text into other formats
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-WikiFormat
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Text-WikiFormat-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl-generators
# /oreon:deps
%description
The original Wiki web site had a very simple interface to edit and to
add pages.  Its formatting rules are simple and easy to use.  They are
also easy to translate into other, more complicated markup languages
with this module.  It creates HTML by default, but can produce valid
POD, DocBook, XML, or any other format imaginable.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-WikiFormat-%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

PERL_RUN_ALL_TESTS=1 ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
