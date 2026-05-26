%if 0%{?fedora} > 35 || 0%{?oreon}
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-quh
Summary: Quechua, South Bolivia hunspell dictionaries
%global upstreamid 20110816
Version: 0.%{upstreamid}
Release: 32%{?dist}
# Following links are dead now
# don't report any bugs
Source: http://www.runasimipi.org/quh_BO-pack.zip
# oreon url source checksums begin
%global source0_sha256 d4f4b2033b09c4bc784e4fbe0a395932786938d6f5f8e278b8fb64f641899434
%global source0_file quh_BO-pack.zip
# oreon url source checksums end
URL: http://www.runasimipi.org/blanco-en.php?file=desarrollar-orto
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-quh)

%description
Quechua South Bolivia hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/quh_BO-pack.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d4f4b2033b09c4bc784e4fbe0a395932786938d6f5f8e278b8fb64f641899434" || { echo "oreon: Source0 SHA256 mismatch for quh_BO-pack.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n quh_BO-pack
unzip -qq quh_BO.zip

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p quh_BO/quh_BO.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc quh_BO/Copyright quh_BO/README_quh_BO.txt
%license quh_BO/COPYING
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20110816-32
- Import
