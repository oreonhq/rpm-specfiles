%global source0_hash 1626aaf2b428ebcc6112abe742e95d4ebcc6576af65fad3ba2d32ddb403f3049
%global source1_hash e17d7c89fc5479198692d73aef8c23edd20d441347311a79befd67f79be62c28

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-sw
Summary: Swahili hunspell dictionaries
%global upstreamid 20050819
Version: 0.%{upstreamid}
Release: 36%{?dist}
Source0:        https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/sw_TZ/sw_TZ.aff
Source1:        https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/sw_TZ/sw_TZ.dic
URL: http://www.it46.se
License: LGPL-2.1-or-later
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-sw)

%description
Swahili hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -c -T

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sw_TZ.aff
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sw_TZ.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
sw_TZ_aliases="sw_KE"
for lang in $sw_TZ_aliases; do
        ln -s sw_TZ.aff $lang.aff
        ln -s sw_TZ.dic $lang.dic
done
popd


%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20050819-36
- Import
