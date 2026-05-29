%global source0_hash f48cb8a7ec86b94fe7383fd0c781c83b69c57b595cb10a6a69a5444f4f2368a7

Name: hyphen-nl
Summary: Dutch hyphenation rules
%global upstreamid 20050617
Version: 0.%{upstreamid}
Release: 36%{?dist}
Source:        hyph_nl_NL.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL-2.0-only
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-nl)

%description
Dutch hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hyphen-nl

%build
for i in README_hyph_nl_NL.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_nl_NL.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
nl_NL_aliases="nl_AW nl_BE"
for lang in $nl_NL_aliases; do
        ln -s hyph_nl_NL.dic hyph_$lang.dic
done


%files
%doc README_hyph_nl_NL.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20050617-36
- Import
