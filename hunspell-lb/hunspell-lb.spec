%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-lb
Summary: Luxembourgish hunspell dictionaries
%global upstreamid 20121128
Version: 0.%{upstreamid}
Release: 28%{?dist}
Source: http://downloads.spellchecker.lu/packages/OOo3/SpellcheckerLu.oxt
URL: http://spellchecker.lu
License: EUPL-1.1
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-lb)

%description
Luxembourgish hunspell dictionaries.

%package -n mythes-lb
Summary: Luxembourgish thesaurus
Requires: mythes
Supplements: (mythes and langpacks-lb)

%description -n mythes-lb
Luxembourgish thesaurus.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_lb_LU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes


%files
%doc registration/README_lb_LU.txt
%{_datadir}/%{dict_dirname}/*

%files -n mythes-lb
%doc registration/README_lb_LU.txt
%{_datadir}/mythes/th_lb_LU_v2.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-28
- Prepare for Oreon 11 (RP1)
