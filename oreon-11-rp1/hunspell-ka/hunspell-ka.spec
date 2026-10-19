%global source0_hash d7ad24a9b84b8e2431ed0f1ffa39a720fbcd967b92d84eb92291d2af9dfd2551
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon} >= 11
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
Name: hunspell-ka
Summary:        Georgian hunspell dictionaries
Version: 0.1
Release:        1%{?dist}
Source0:        https://github.com/gamag/ka_GE.spell/archive/refs/tags/%{version}.tar.gz#/ka_GE-%{version}.tar.gz
URL: https://github.com/gamag/ka_GE.spell/
License: MIT AND CC-BY-4.0
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ka)
# oreon:deps

# /oreon:deps
%description
Georgian hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ka_GE.spell-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/*.dic dictionaries/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-5
- Prepare for Oreon 11 (RP1)
