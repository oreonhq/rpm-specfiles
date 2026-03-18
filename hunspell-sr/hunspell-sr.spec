%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-sr
Summary: Serbian hunspell dictionaries
%global upstreamid 20130715
Version: 0.%{upstreamid}
Release: 2%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/1572/9/dict-sr.oxt
URL: http://extensions.services.openoffice.org/project/dict-sr
License: LGPL-3.0-only
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-sr)
Provides: hunspell-bs = %{version}-%{release}

%description
Serbian hunspell dictionaries.

%package -n hyphen-sr
Requires: hyphen
Summary: Serbian hyphenation rules
Provides: hyphen-bs = %{version}-%{release}
Supplements: (hyphen and langpacks-sr)

%description -n hyphen-sr
Serbian hyphenation rules.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p sr.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sr_YU.dic
cp -p sr.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sr_YU.aff
cp -p sr-Latn.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sh_YU.dic
cp -p sr-Latn.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sh_YU.aff

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_sr_YU.dic
cp -p hyph_sr-Latn.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_sh_YU.dic

sr_YU_aliases="sr_ME sr_RS"
sh_YU_aliases="sh_ME sh_RS bs_BA"

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
for lang in $sr_YU_aliases; do
	ln -s sr_YU.aff $lang.aff
	ln -s sr_YU.dic $lang.dic
done
for lang in $sh_YU_aliases; do
	ln -s sh_YU.aff $lang.aff
	ln -s sh_YU.dic $lang.dic
done
popd

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
for lang in $sr_YU_aliases; do
	ln -s hyph_sr_YU.dic "hyph_"$lang".dic"
done
for lang in $sh_YU_aliases; do
	ln -s hyph_sh_YU.dic "hyph_"$lang".dic"
done
popd


%files
%doc registration/license*.txt
%{_datadir}/%{dict_dirname}/*

%files -n hyphen-sr
%doc registration/license*.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-2
- Prepare for Oreon 11 (RP1)
