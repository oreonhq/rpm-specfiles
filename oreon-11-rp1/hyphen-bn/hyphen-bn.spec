%global source0_hash 1a77d2d57f74cc87343ac30f77d04a0a035821361c805063e374f6c0486bfab9

Name: hyphen-bn
Summary: Bengali hyphenation rules
Epoch: 1
Version: 0.7.0
Release: 29%{?dist}
Source:        http://download.savannah.gnu.org/releases/smc/hyphenation/patterns/hyphen-bn-0.7.0.tar.bz2
URL: http://wiki.smc.org.in
License: LGPL-3.0-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-bn)

%description
Bengali hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build

%install
mkdir -p  %{buildroot}/%{_datadir}/hyphen
install -m644 -p *.dic %{buildroot}/%{_datadir}/hyphen

pushd %{buildroot}/%{_datadir}/hyphen/
bn_IN_aliases="bn_BD"
for lang in $bn_IN_aliases; do
        ln -s hyph_bn_IN.dic hyph_$lang.dic
done
popd

%files
%doc README COPYING ChangeLog
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-29
- Prepare for Oreon 11 (RP1)
