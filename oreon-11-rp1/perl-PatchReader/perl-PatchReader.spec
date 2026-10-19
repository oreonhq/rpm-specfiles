%global source0_hash b8de37460347bb5474dc01916ccb31dd2fe0cd92242c4a32d730e8eb087c323c
Name:		perl-PatchReader
Version: 	0.9.6
Release:        1%{?dist}
Summary:        Utilities to read and manipulate patches and CVS
License: 	LicenseRef-Callaway-MPLv1.1 AND Artistic-2.0
URL: 		https://metacpan.org/release/PatchReader
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEISER/PatchReader-%{version}.tar.gz
BuildArch: 	noarch
Requires:       cvs
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
PatchReader is a set of utilities for reading in, transforming, and doing
various other things with a patch.  It basically allows you to create a
chain of readers that can read a patch, remove files from a patch, add
CVS context, fix up the patch root according to CVS, and output the patch
as raw unified or through a template processor (used in some places to
output a patch as HTML).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PatchReader-%{version}
chmod 644 Changes README
find . -name "*.pm" | xargs chmod 644
%{__perl} -pi -e 's/\r//g' Changes README

%build

%{__perl} Makefile.PL INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}
%install
%{__rm} -rf ${RPM_BUILD_ROOT}
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
