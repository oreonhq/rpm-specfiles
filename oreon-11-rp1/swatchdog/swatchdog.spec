%global source0_hash 5bb644d3750ee89b9aecab797df66b28b9fd174a5f0f96cd62367af8975b4f63

%global oldname swatch
%global newname swatchdog

Name:           %{newname}
Version:        3.2.4
Release:        7%{?dist}
Summary:        Tool for actively monitoring log files
License:        GPL-2.0-or-later
URL:            http://swatch.sourceforge.net/
Source0:        http://download.sf.net/swatch/%{newname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(File::Tail)
BuildRequires:  perl(ExtUtils::MakeMaker)
# https://sourceforge.net/p/swatch/patches/13/
Patch0:         swatchdog-3.2.4-manpage-fix.patch
# https://sourceforge.net/p/swatch/patches/14/
Patch1:         swatchdog-3.2.4-no-more-zombies.patch
# https://sourceforge.net/p/swatch/patches/15/
Patch2:         swatchdog-3.2.4-more-cleanups.patch
# https://sourceforge.net/p/swatch/patches/16/
Patch3:         swatchdog-3.2.4-mail-at-fix.patch
# https://sourceforge.net/p/swatch/patches/17/
Patch4:         swatchdog-3.2.4-fsf-address-fix.patch
Provides:       %{oldname} = %{version}-%{release}
Obsoletes:      %{oldname} <= 3.2.3-39

%description
The Simple WATCHdog started out as swatch, the "simple watchdog"
for activity monitoring log files produced by UNIX's syslog
facility. It has since been evolving into a utility that can
monitor just about any type of log. The name has been changed to
satisfy a request made by the old Swiss watch company.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fix
%patch -P1 -p1 -b .zombies
%patch -P2 -p1 -b .more-cleanups
%patch -P3 -p1 -b .mail-at-fix
%patch -P4 -p1 -b .address-fix
# chmod -v 644 tools/*

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
chmod -R u+w %{buildroot}/*

%check
make test

%files
%license COPYRIGHT COPYING
%doc CHANGES KNOWN_BUGS README examples/ tools/
%{_bindir}/swatchdog
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Swatchdog/
# Not sure why we own this, but okay, sure.
%dir %{perl_vendorlib}/auto
%{perl_vendorlib}/auto/Swatchdog/

%changelog
%autochangelog
