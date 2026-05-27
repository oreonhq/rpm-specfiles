%global source0_hash 8bc8b1c8a71c82e98c418d7d66217359669569e81e0e679f4756bcac67d71e0d

Name: mythes-en
Summary: English thesaurus
Version: 3.0
Release: 43%{?dist}
Source: http://www.danielnaber.de/wn2ooo/wn2ooo20050723.tgz
URL: http://www.danielnaber.de/wn2ooo/
BuildRequires: python3-devel
BuildRequires: perl-interpreter
BuildRequires: wordnet = %{version}
# License BSD is for the th_gen_idx.pl file
# License Artistic Clarified is for python files
License: BSD-3-Clause-Modification AND ClArtistic
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-en)

Patch0: mythes-en.python3.patch

%description
English thesaurus.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c %{name}-%{version}
%patch -P0 -p1 -b .python3

%build
export WNHOME=/usr/share/wordnet-%{version}
python3 wn2ooo/wn2ooo.py > th_en_US_v2.dat
cat th_en_US_v2.dat | perl wn2ooo/th_gen_idx.pl > th_en_US_v2.idx


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_en_US_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
en_US_aliases="en_AG en_AU en_BS en_BW en_BZ en_CA en_DK en_GB en_GH en_IE en_IN en_JM en_MW en_NA en_NG en_NZ en_PH en_SG en_TT en_ZA en_ZM en_ZW"
for lang in $en_US_aliases; do
        ln -s th_en_US_v2.idx "th_"$lang"_v2.idx"
        ln -s th_en_US_v2.dat "th_"$lang"_v2.dat"
done
popd


%files
%doc wn2ooo/LICENSE_th_gen_idx.txt wn2ooo/README.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-43
- Prepare for Oreon 11 (RP1)
