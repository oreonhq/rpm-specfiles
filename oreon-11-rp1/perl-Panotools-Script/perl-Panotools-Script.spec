%global source0_hash 95507d1e75ed1389cacd7731a1e62697c386eb71ea5ae2bf50ff7f70320c1f0a

Name:           perl-Panotools-Script
Version:        0.29
Release:        21%{?dist}
Summary:        Library for manipulating Hugin .pto files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Panotools-Script
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPOSTLE/Panotools-Script-%{version}.tar.gz
Source1:        panotools-script.png
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::UserAgent) >= 5
BuildRequires:  perl(URI) >= 1
BuildRequires:  perl(Image::Size) >= 2.9
BuildRequires:  perl(Image::ExifTool) >= 6
BuildRequires:  perl(Math::Trig)
Requires:       perl(LWP::UserAgent) >= 5
Requires:       perl(URI) >= 1
Requires:       perl(Image::Size) >= 2.9
Requires:       perl(Image::ExifTool) >= 9.07
Requires:       perl(Math::Trig)
# added manually
Requires:       hugin-base libpano13-tools ImageMagick enblend zenity autotrace
BuildRequires:  perl(Test::More) desktop-file-utils

%description
Library and utilities for manipulating project files created by the Hugin photo
stitching software.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Panotools-Script-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# added manually
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps
%{__install} -m0644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
sed -i 's/hugin.png/panotools-script.png/' desktop/*.desktop
desktop-file-install --vendor="" \
  --dir=%{buildroot}/%{_datadir}/applications desktop/*.desktop

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*
# added manually
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/panotools-script.png
%{_mandir}/man1/*

%changelog
%autochangelog
