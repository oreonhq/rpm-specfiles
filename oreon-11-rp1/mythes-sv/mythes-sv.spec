%global source0_hash none

Name: mythes-sv
Summary: Swedish thesaurus
Version: 1.3
Release: 32%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/934/4/swedishthesaurus.oxt
URL: http://extensions.services.openoffice.org/project/SweThes
License: MIT
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-sv)

%description
Swedish thesaurus.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_sv_SE.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_sv_SE_v2.dat
cp -p dictionaries/th_sv_SE.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_sv_SE_v2.idx
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s th_sv_SE_v2.dat "th_"$lang"_v2.dat"
        ln -s th_sv_SE_v2.idx "th_"$lang"_v2.idx"
done
popd


%files
%doc Info-en.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-32
- Prepare for Oreon 11 (RP1)
