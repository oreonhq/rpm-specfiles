Name: mythes-sk
Summary: Slovak thesaurus
%global upstreamid 20130130
Version: 0.%{upstreamid}
Release: 29%{?dist}
Source: http://www.sk-spell.sk.cx/thesaurus/download/OOo-Thesaurus2-sk_SK.zip
# oreon url source checksums begin
%global source0_sha256 c761d15c2b4ade5fe38f68f61c15d6535c8a3be78c30669c3349f1847bc7437a
%global source0_file OOo-Thesaurus2-sk_SK.zip
# oreon url source checksums end
URL: http://www.sk-spell.sk.cx/thesaurus/
License: MIT
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-sk)

%description
Slovak thesaurus.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/OOo-Thesaurus2-sk_SK.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c761d15c2b4ade5fe38f68f61c15d6535c8a3be78c30669c3349f1847bc7437a" || { echo "oreon: Source0 SHA256 mismatch for OOo-Thesaurus2-sk_SK.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -c

%build
for i in README_th_sk_SK_v2.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_sk_SK_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes


%files
%doc README_th_sk_SK_v2.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-29
- Prepare for Oreon 11 (RP1)
