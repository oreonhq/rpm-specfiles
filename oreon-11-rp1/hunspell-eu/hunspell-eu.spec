# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 12934d021558bf001c0bcaf0a1fc6f08ce6c7e8b7d48a8cb0bfe31763f0f5988
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-eu
Summary: Basque hunspell dictionaries
Version: 5.1
Release: 15%{?dist}
Source0: http://xuxen.eus/static/hunspell/xuxen_%{version}_hunspell.zip
URL: http://xuxen.eus
License: LGPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-eu)

%description
Basque hunspell dictionaries.

%prep
%oreon_verify_sources
%setup -q -c -n hunspell-eu

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
cp -p eu_ES.dic %{buildroot}%{_datadir}/%{dict_dirname}/eu_ES.dic
cp -p eu_ES.aff %{buildroot}%{_datadir}/%{dict_dirname}/eu_ES.aff


%files
%license LICENSE.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1-15
- Prepare for Oreon 11 (RP1)
