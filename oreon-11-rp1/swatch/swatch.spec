%global source0_hash e29480993e52f245f3abec079b3103d8e97244dafe754f8c2d37e7b0b3b58077
Name:           swatch
Version:        3.2.3
Release:        1%{?dist}
Summary:        Tool for actively monitoring log files
License:        GPL-2.0-or-later
URL:            http://swatch.sourceforge.net/
Source0:        http://download.sf.net/swatch/swatch-%{version}.tar.gz
BuildArch:      noarch
Patch0:         swatch-3.2.3-manpage-fix.patch
Patch1:		swatch-3.2.3-no-more-zombies.patch
Patch2:		swatch-3.2.3-more-cleanups.patch
Patch3:		swatch-3.2.3-mail-at-fix.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Tail)
BuildRequires:  perl-generators
# /oreon:deps
%description
The Simple WATCHer is an automated monitoring tool that is capable
of alerting system administrators of anything that matches the
patterns described in the configuration file, whilst constantly
searching logfiles using perl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fix
%patch -P1 -p1 -b .zombies
%patch -P2 -p1 -b .more-cleanups
%patch -P3 -p1 -b .mail-at-fix
chmod -v 644 tools/*

%{?filter_from_requires: %filter_from_requires /^perl(Mail:Sendmail)$/d }
%{?filter_from_requires: %filter_from_requires /^perl(Sys:Hostname)$/d }
%{?perl_default_filter}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist  -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
