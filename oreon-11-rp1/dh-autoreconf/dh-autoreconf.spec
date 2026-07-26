%global source0_hash 5cbd797955824105a16eefcafc4a92eacc556372a69de744b504877723a7ab0e

Name:           dh-autoreconf
Version:        21
Release:        4%{?dist}
Summary:        debhelper add-on to call autoreconf and clean up after the build

BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/dh-autoreconf
Source0:        http://ftp.de.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz

BuildRequires:  perl-generators
BuildRequires:  perl(Pod::Text)

Requires:       debhelper
Requires:       autoconf
Requires:       automake
Requires:       libtool
# For /usr/bin/autopoint
Requires:       gettext-devel

%description
dh-autoreconf provides a debhelper sequence addon named 'autoreconf' and two
commands, dh_autoreconf and dh_autoreconf_clean.
 * The dh_autoreconf command creates a list of the files and their checksums,
   calls autoreconf and then creates a second list for the new files.
 * The dh_autoreconf_clean command compares these two lists and removes all
   files which have been added or changed (files may be excluded if needed).
For CDBS users, a rule is provided to call the dh-autoreconf programs at the
right time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n work

%build
# Build manpages
pod2man --section=1 dh_autoreconf dh_autoreconf.1
pod2man --section=1 dh_autoreconf_clean dh_autoreconf_clean.1
pod2man --section=7 dh-autoreconf.pod dh-autoreconf.7

%install
install -Dpm 0755 dh_autoreconf %{buildroot}%{_bindir}/dh_autoreconf
install -Dpm 0755 dh_autoreconf_clean %{buildroot}%{_bindir}/dh_autoreconf_clean
install -Dpm 0644 autoreconf.pm %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Sequence/autoreconf.pm
install -Dpm 0644 autoreconf.mk %{buildroot}%{_datadir}/cdbs/1/rules/autoreconf.mk
install -Dpm 0644 ltmain-as-needed.diff %{buildroot}%{_datadir}/%{name}/ltmain-as-needed.diff
install -Dpm 0644 dh_autoreconf.1 %{buildroot}%{_mandir}/man1/dh_autoreconf.1
install -Dpm 0644 dh_autoreconf_clean.1 %{buildroot}%{_mandir}/man1/dh_autoreconf_clean.1
install -Dpm 0644 dh-autoreconf.7 %{buildroot}%{_mandir}/man7/dh-autoreconf.7

%files
%license debian/copyright
%{_bindir}/dh_autoreconf
%{_bindir}/dh_autoreconf_clean
%{perl_vendorlib}/*
%{_datadir}/cdbs/1/rules/autoreconf.mk
%{_datadir}/%{name}/
%{_mandir}/man1/dh_autoreconf.1*
%{_mandir}/man1/dh_autoreconf_clean.1*
%{_mandir}/man7/dh-autoreconf.7*

%changelog
%autochangelog
