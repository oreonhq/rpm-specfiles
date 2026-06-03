%global source0_hash ab53d76a82da5229d484ce0d4c892f6c1ffba5fddeb7bac73685cbf590ae130d
%global source1_hash f3e8877d0f7f12c3ab7ef812388a77c20a9fcd3f8cc24d973709ec517150598d

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ne
Summary: Nepali hunspell dictionaries
Version: 20080425
Release: 36%{?dist}
Source0:        https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/ne_NP/ne_NP.aff
Source1:        https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/ne_NP/ne_NP.dic
URL: http://nepalinux.org/downloads
License: LGPL-2.1-only
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ne)

%description
Nepali hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -c -T
cp -p %{SOURCE0} ne_NP.aff
cp -p %{SOURCE1} ne_NP.dic
sed -i 's|चलन/चल्ती/15,22|चलनचल्ती/15,22|g' ne_NP.dic
sed -i 's|निजामती/I15,22|निजामती/15,22|g' ne_NP.dic
sed -i 's/\r//;s/[ \t]*$//' ne_NP.dic

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ne_NP.aff ne_NP.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
ne_NP_aliases="ne_IN"
for lang in $ne_NP_aliases; do
        ln -s ne_NP.aff $lang.aff
        ln -s ne_NP.dic $lang.dic
done
popd

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20080425-36
- Import
