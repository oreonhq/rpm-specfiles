Name:           perl-Font-AFM
Version:        1.20
Release:        52%{?dist}
Summary:        Perl interface to Adobe Font Metrics files

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Font-AFM
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/Font-AFM-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 32671166da32596a0f6baacd0c1233825a60acaf25805d79c81a3f18d6088bc1
%global source0_file Font-AFM-1.20.tar.gz
# oreon url source checksums end


BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 11
# REGRESSION: dnf5 is unable to BuildRequires: files
BuildRequires: urw-base35-nimbus-sans-fonts
%else
# This is what is actually BuildRequired
BuildRequires:  %{_fontbasedir}/urw-base35/NimbusSans-Bold.afm
%endif

%description
Interface to Adobe Font Metrics files

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Font-AFM-1.20.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "32671166da32596a0f6baacd0c1233825a60acaf25805d79c81a3f18d6088bc1" || { echo "oreon: Source0 SHA256 mismatch for Font-AFM-1.20.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Font-AFM-%{version}
# We don't have Helvetica, use NimbusSans-Bold.afm instead
sed -i -e 's,Helvetica,NimbusSans-Bold,g' t/afm.t
# Change the expected string width to match NimbusSans-Bold.
# 4558 is a sum of widths of characters from testing 'Gisle Aas' string
# in NimbusSans-Bold - see NimbusSans-Bold.afm for specific character
# length.
sed -i -e 's,4279,4558,g' t/afm.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*


%check
%{__make} test METRICS=%{_fontbasedir}/urw-base35


%files
%doc Changes README
%{perl_vendorlib}/Font
%{_mandir}/man3/Font*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20-52
- Prepare for Oreon 11 (RP1)
