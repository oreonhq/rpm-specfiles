%global source0_hash f2590758ef3afe088e9f130d8987b150af99369cb7293936f163d60578a5c21a

%global pkgname iXhash2

Summary:        SpamAssassin plugin to lookup e-mail checksums in blacklists
Name:           spamassassin-%{pkgname}
Version:        4.00
Release:        6%{?dist}
License:        Apache-2.0
URL:            https://mailfud.org/%{pkgname}/
Source0:        https://mailfud.org/%{pkgname}/%{pkgname}-%{version}.tar.gz
Source1:        spamassassin-iXhash2.eml
Patch0:         spamassassin-iXhash2-4.00-conf.patch
Requires:       spamassassin >= 4.0.0
Provides:       spamassassin-iXhash = 1.5.5-2
Obsoletes:      spamassassin-iXhash < 1.5.5-2
BuildRequires:  %{_bindir}/perldoc
BuildRequires:  perl-generators
BuildArch:      noarch

%description
iXhash2 is an unofficial improved version of the iXhash spam filter
plugin for SpamAssassin, adding async DNS lookups for performance and
removing unneeded features but fully compatible with the iXhash 1.5.5
(https://sourceforge.net/projects/ixhash/) implementation. It computes
MD5 checksums of fragments of the body of an e-mail and compares them
to those of known spam using DNS queries to a RBL-like name server. So
it works similar to the standard plugins that use the Pyzor, Razor and
DCC software packages from within SpamAssassin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}
%patch -P0 -p1 -b .conf
cp -pf %{SOURCE1} iXhash2.eml

%build

%install
install -D -p -m 644 %{pkgname}.cf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/%{pkgname}.cf
touch -c -r %{pkgname}.cf.conf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/%{pkgname}.cf
install -D -p -m 644 %{pkgname}.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/SpamAssassin/Plugin/%{pkgname}.pm
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
perldoc %{pkgname}.pm > $RPM_BUILD_ROOT%{_mandir}/man3/Mail::SpamAssassin::Plugin::%{pkgname}.3pm

%files
%license LICENSE
%doc CHANGELOG README iXhash2.eml
%config(noreplace) %{_sysconfdir}/mail/spamassassin/%{pkgname}.cf
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/%{pkgname}.pm
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
