Name:      	perl-Class-ReturnValue
Summary:   	Class::ReturnValue Perl module
Version:   	0.55
Release:   	50%{?dist}
License:   	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:       	https://metacpan.org/release/Class-ReturnValue

BuildArch: 	noarch
Source:    	https://cpan.metacpan.org/authors/id/J/JE/JESSE/Class-ReturnValue-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 ed3836885d78f734ccd7a98550ec422a616df7c31310c1b7b1f6459f5fb0e4bd
%global source0_file Class-ReturnValue-0.55.tar.gz
# oreon url source checksums end

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:  perl(Exporter)
# Tests
BuildRequires:	perl(Test::More)

%description
A return-value object that lets you treat it as as a boolean, array or object.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Class-ReturnValue-0.55.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ed3836885d78f734ccd7a98550ec422a616df7c31310c1b7b1f6459f5fb0e4bd" || { echo "oreon: Source0 SHA256 mismatch for Class-ReturnValue-0.55.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Class-ReturnValue-%{version} 
rm -r inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/Class
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.55-50
- Prepare for Oreon 11 (RP1)
