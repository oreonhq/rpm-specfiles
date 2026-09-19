%global source0_hash b7258d927549b45bac879a57df18ca53bfc3374228ad5b30f8019fb1def2f6d1

Name:           perl-Kwiki-Attachments
Version:        0.21
Release:        45%{?dist}
Summary:        Kwiki Page Attachments Plugin
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki-Attachments
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SUE/Kwiki-Attachments-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(File::Basename)
# XXX: BuildRequires:  perl(Image::Magick)
# XXX: BuildRequires:  perl(Imager)
BuildRequires:  perl(Kwiki::CGI)
BuildRequires:  perl(Kwiki::Installer)
BuildRequires:  perl(Kwiki::Plugin)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Spoon::Formatter::WaflPhrase)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(Kwiki) >= 0.37
Recommends:     perl(Imager)
Suggests:       perl(Image::Magick)

%description
This module gives a Kwiki wiki the ability to upload, store and manage file
attachments on any page. Thumbnails will be created for supported file
types if Imager or Image::Magick is installed. For more information, read
the module POD.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Kwiki-Attachments-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
