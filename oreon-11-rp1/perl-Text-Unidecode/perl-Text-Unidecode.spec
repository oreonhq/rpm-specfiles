Name:           perl-Text-Unidecode
Version:        1.30
Release:        28%{?dist}
Summary:        US-ASCII transliterations of Unicode text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Unidecode
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBURKE/Text-Unidecode-1.30.tar.gz
# oreon url source checksums begin
%global source0_sha256 6c24f14ddc1d20e26161c207b73ca184eed2ef57f08b5fb2ee196e6e2e88b1c6
%global source0_file Text-Unidecode-1.30.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test)
BuildRequires:  perl(Text::Wrap)

%description

Text::Unidecode provides a function, `unidecode(...)' that takes
Unicode data and tries to represent it in US-ASCII characters (i.e.,
the universally displayable characters between 0x00 and 0x7F). The
representation is almost always an attempt at *transliteration* -- i.e.,
conveying, in Roman letters, the pronunciation expressed by the text in
some other writing system.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Text-Unidecode-1.30.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6c24f14ddc1d20e26161c207b73ca184eed2ef57f08b5fb2ee196e6e2e88b1c6" || { echo "oreon: Source0 SHA256 mismatch for Text-Unidecode-1.30.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Text-Unidecode-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README TODO.txt ChangeLog
%{perl_vendorlib}/Text/
%{_mandir}/man3/*.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.30-28
- Import
