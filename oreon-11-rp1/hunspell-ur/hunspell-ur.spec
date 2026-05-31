%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ur
Summary: Urdu hunspell dictionaries
Version: 0.64
Release: 35%{?dist}
#http://urdudictionary.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=30004#DownloadId=74761
#and click yes to agree to LGPLv2+, which stinks as a download-url :-(
Source: UrduDictionary.xpi
# This URL is dead now
URL: http://urdudictionary.codeplex.com
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ur)

%description
Urdu hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n hunspell-ur

%build
# nothing here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/ur.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ur_PK.aff
cp -p dictionaries/ur.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ur_PK.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
ur_PK_aliases="ur_IN"
for lang in $ur_PK_aliases; do
        ln -s ur_PK.aff $lang.aff
        ln -s ur_PK.dic $lang.dic
done
popd


%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.64-35
- Import
