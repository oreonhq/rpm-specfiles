Name: hyphen-gu
Summary: Gujarati hyphenation rules
Epoch: 1
Version: 0.7.0
Release: 29%{?dist}
Source: http://download.savannah.gnu.org/releases/smc/hyphenation/patterns/%{name}-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 901b23e07edf6b5030ca3e584b80642ab663090f66975d4f729d7306182eb799
%global source0_file hyphen-gu-0.7.0.tar.bz2
# oreon url source checksums end
URL: http://wiki.smc.org.in
License: LGPL-3.0-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-gu)

%description
Gujarati hyphenation rules.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/hyphen-gu-0.7.0.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "901b23e07edf6b5030ca3e584b80642ab663090f66975d4f729d7306182eb799" || { echo "oreon: Source0 SHA256 mismatch for hyphen-gu-0.7.0.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/hyphen
install -m644 -p *.dic %{buildroot}/%{_datadir}/hyphen

%files
%doc README COPYING ChangeLog
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-29
- Prepare for Oreon 11 (RP1)
