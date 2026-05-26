%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-gu
Summary: Gujarati hunspell dictionaries
Version: 1.0.0
Release: 28%{?dist}
Epoch: 1
Source: http://anishpatil.fedorapeople.org/gu_in.%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 49b4b9323dd8728b4350c5240708dfc6ac89a09355b011a6bbedc3b49ed889af
%global source0_file gu_in.1.0.0.tar.gz
# oreon url source checksums end
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
License: GPL-1.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-gu)

%description
Gujarati hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gu_in.1.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "49b4b9323dd8728b4350c5240708dfc6ac89a09355b011a6bbedc3b49ed889af" || { echo "oreon: Source0 SHA256 mismatch for gu_in.1.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -c -n gu_IN

%build


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p gu_IN/gu_IN.dic gu_IN/gu_IN.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc gu_IN/README_gu_IN.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-28
- Prepare for Oreon 11 (RP1)
