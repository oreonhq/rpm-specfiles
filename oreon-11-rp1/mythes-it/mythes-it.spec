%global source0_hash none

Name:         mythes-it
Summary:      Italian thesaurus
Version:      5.1.1
Release:      %autorelease
# The license text is embedded within the README files
# Here we specify the thesaurus license only as other files are not packaged 
License:      GPL-3.0-only
URL:          https://pagure.io/dizionario_italiano
Source:        https://download.documentfoundation.org/libreoffice/src/25.2.3/libreoffice-dictionaries-25.2.3.2.tar.xz#/libreoffice-25.2.3.2.tar.xz

BuildArch:    noarch
BuildRequires: mythes-devel
BuildRequires: perl-interpreter
Requires:     mythes
Supplements:  (mythes and langpacks-it)

%description
Italian thesaurus.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2


%build
cd dictionaries/it_IT
th_gen_idx.pl < th_it_IT_v2.dat > th_it_IT_v2.idx


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/it_IT/th_it_IT_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.dat
cp -p dictionaries/it_IT/th_it_IT_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s th_it_IT_v2.dat "th_"$lang"_v2.dat"
        ln -s th_it_IT_v2.idx "th_"$lang"_v2.idx"
done


%files
%doc dictionaries/it_IT/README_th_it_IT.txt dictionaries/it_IT/CHANGELOG.txt
%{_datadir}/mythes/th_it_IT_v2.*
%{_datadir}/mythes/th_it_CH_v2.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.1-1
- Prepare for Oreon 11 (RP1)
