%global source0_hash 555ddffde22da3c86d1caf5a9c1fb8a152ac2b84730437bd39cc08849c9f4852
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:           quilt
Version:        0.69
Release:        3%{?dist}
Summary:        Scripts for working with series of patches
License:        GPL-2.0-only
URL:            https://savannah.nongnu.org/projects/%{name}
Source0:        https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bzip2
Requires:       coreutils
Requires:       diffstat
Requires:       diffutils
Requires:       gawk
Requires:       gzip
Requires:       p7zip
Requires:       procmail
Requires:       rpm-build
Requires:       sed
Requires:       tar
Requires:       util-linux-ng
Requires:       %{_sbindir}/sendmail
# oreon:deps
BuildRequires:  /usr/sbin/sendmail
BuildRequires:  diffstat
BuildRequires:  gawk
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  p7zip
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  util-linux-ng
# /oreon:deps
%description
These scripts allow one to manage a series of patches by keeping track of the
changes each patch makes. Patches can be applied, un-applied, refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts found at
http://www.zip.com.au/~akpm/linux/patches/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure                             \
  --docdir=%{_pkgdocdir}               \
  --with-diffstat=%{_bindir}/diffstat  \
  --with-sendmail=%{_sbindir}/sendmail \
;
%make_build
%install
%make_install BUILD_ROOT=%{buildroot}
%{find_lang} %{name}
mv %{buildroot}%{_pkgdocdir}/* .
rm -rf %{buildroot}%{_pkgdocdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
