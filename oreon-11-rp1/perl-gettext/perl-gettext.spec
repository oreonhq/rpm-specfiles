# This package should be renamed into perl-Locale-gettext
%global tarname Locale-gettext

Name:           perl-gettext
Version:        1.07
Release:        37%{?dist}
Summary:        Interface to gettext family of functions

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/gettext
Source0:        https://cpan.metacpan.org/authors/id/P/PV/PVANDRY/%{tarname}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 909d47954697e7c04218f972915b787bd1244d75e3bd01620bc167d5bbc49c15
%global source0_file Locale-gettext-1.07.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  gettext
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(POSIX)

# Optional
BuildRequires:  perl(Encode)
# Tests:
BuildRequires:  perl(Test)

# Need to allow LANG=en_US.UTF-8
# Testsuite fails w/ LANG=C.UTF-8 on fedora >= 40
BuildRequires:  glibc-langpack-en

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software.


%package -n perl-%{tarname}
Summary:        %{summary}

%description -n perl-%{tarname}
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Locale-gettext-1.07.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "909d47954697e7c04218f972915b787bd1244d75e3bd01620bc167d5bbc49c15" || { echo "oreon: Source0 SHA256 mismatch for Locale-gettext-1.07.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{tarname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
# Testsuite fails w/ LANG=C.UTF-8 on fedora >= 40
LANG=en_US.UTF-8 %{__make} test


%files -n perl-%{tarname}
%doc README
%{perl_vendorarch}/auto/Locale
%{perl_vendorarch}/Locale
%{_mandir}/man3/*.3*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.07-37
- Prepare for Oreon 11 (RP1)
