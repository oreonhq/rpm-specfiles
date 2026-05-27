%global source0_hash 966faf94e7d05d52e9afdd20b266e28932edf5b32fe26aa83d554d6a2c6021ea

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

%global ver_date 2014-11-08

Summary: Arabic hunspell dictionaries
Name: hunspell-ar
Version: 3.5
Release: 26%{?dist}
License: GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1

URL: http://ayaspell.sourceforge.net/
Source: http://sourceforge.net/projects/ayaspell/files/hunspell-ar_%{version}.%{ver_date}.zip

BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ar)

%description
Arabic (Egypt, Algeria, etc.) hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ar.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ar_TN.dic
cp -p ar.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ar_TN.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
ar_TN_aliases="ar_AE ar_BH ar_DJ ar_DZ ar_EG ar_ER ar_IL ar_IN ar_IQ ar_JO ar_KM ar_KW ar_LB ar_LY ar_MA ar_MR ar_OM ar_PS ar_QA ar_SA ar_SD ar_SO ar_SY ar_TD ar_YE"
for lang in $ar_TN_aliases; do
    ln -s ar_TN.aff $lang.aff
    ln -s ar_TN.dic $lang.dic
done
popd

%files
%doc AUTHORS ChangeLog-ar COPYING README-* THANKS
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.5-26
- Prepare for Oreon 11 (RP1)
