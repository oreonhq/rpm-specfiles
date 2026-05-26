# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 c72f2ea4758e7a2bb9ef5a7e9e33fb8b387deb2669e66203b4020176d38c3e60
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-az
Summary: Azerbaijani hunspell dictionaries
# date is derived from upstream az.dic file timestamp
%global upstreamid 20180807
Version: 0.%{upstreamid}
Release: 8%{?dist}
Source: https://github.com/mozillaz/spellchecker/archive/refs/heads/master.zip#/azerbaijani_spellchecker-0.2.zip
URL: https://github.com/mozillaz/spellchecker/
License: MPL-2.0
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-az)

%description
Azerbaijani hunspell dictionaries.

%prep
%oreon_verify_sources
%autosetup -n spellchecker-master

%build
# nothing here to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/*.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/az_AZ.dic
cp -p dictionaries/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/az_AZ.aff

%files
%doc LICENSE README.md
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-8
- Prepare for Oreon 11 (RP1)
