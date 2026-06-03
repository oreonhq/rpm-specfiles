%global source0_hash none
%global source1_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fa
Summary: Farsi hunspell dictionaries
%global upstreamid 20070116
Version: 0.%{upstreamid}
Release: 38%{?dist}
Source0: https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/fa_IR/fa_IR.dic
Source1: https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/fa_IR/fa_IR.aff
URL: http://ftp.gnu.org/gnu/aspell/dict/fa
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-fa)

%description
Farsi hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -T

%build
# nothing to build here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fa_IR.dic
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fa_IR.aff

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070116-38
- Import
