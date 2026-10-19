%global source0_hash 95507d1e75ed1389cacd7731a1e62697c386eb71ea5ae2bf50ff7f70320c1f0a
Name:           perl-Panotools-Script
Version:        0.29
Release:        1%{?dist}
Summary:        Library for manipulating Hugin .pto files
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Panotools-Script
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPOSTLE/Panotools-Script-%{version}.tar.gz
Source1:        panotools-script.png
BuildArch:      noarch
Requires:       perl(LWP::UserAgent) >= 5
Requires:       perl(URI) >= 1
Requires:       perl(Image::Size) >= 2.9
Requires:       perl(Image::ExifTool) >= 9.07
Requires:       perl(Math::Trig)
Requires:       hugin-base libpano13-tools ImageMagick enblend zenity autotrace
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Image::ExifTool)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl-generators
# /oreon:deps
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
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps
%{__install} -m0644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
sed -i 's/hugin.png/panotools-script.png/' desktop/*.desktop
desktop-file-install --vendor="" \
  --dir=%{buildroot}/%{_datadir}/applications desktop/*.desktop
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
