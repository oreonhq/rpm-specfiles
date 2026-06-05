%global source0_hash 18fbd01e151af196420b6e63fb996f9d1779e5895e46a254eacd7446be3440ed

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-om
Summary: Oromo hunspell dictionaries
Epoch: 1
Version: 0.04
Release: 34%{?dist}
# Following links are dead now
# Please don't report any bugs for it
URL: http://borel.slu.edu/crubadan/apps.html
License: GPL-3.0-or-later
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-om)

Source0:        https://github.com/openela-main/hunspell-om/raw/el9/SOURCES/hunspell-om-0.04.oxt

%description
Oromo hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
unzip -q %{SOURCE0}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/om_ET.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
om_ET_aliases="om_KE"
for lang in $om_ET_aliases; do
        ln -s om_ET.aff $lang.aff
        ln -s om_ET.dic $lang.dic
done

%files
%doc dictionaries/README_om_ET.txt
%license LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.04-34
- Import
