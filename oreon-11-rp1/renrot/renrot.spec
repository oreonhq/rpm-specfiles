%global source0_hash a3f711787422292693238579a2c139e8ac6367e099ada0815b6b050385f886ae
Name:		renrot
Version:	1.2.0
Release:        1%{?dist}
Summary:        A program to rename and rotate files according to EXIF tags
License:	Artistic-2.0
URL:		http://puszcza.gnu.org.ua/projects/renrot/
Source0:        ftp://download.gnu.org.ua/pub/release/renrot/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	/usr/bin/jpegtran
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Image::ExifTool)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Renrot renames files according the DateTimeOriginal and FileModifyDate
EXIF tags, if they exist. Otherwise, the name will be set according to
the current timestamp. Additionally, it rotates files and their
thumbnails, accordingly Orientation EXIF tag.

The script can also put commentary into the Commentary and UserComment
tags.

Personal details can be specified via XMP tags defined in a
configuration file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*
sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|' $RPM_BUILD_ROOT%{_bindir}/renrot
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m644 etc/colors.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m644 etc/copyright.tag $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m644 etc/renrot.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m644 etc/tags.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
