%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ka
Summary: Georgian hunspell dictionaries
Version: 0.1
Release: 5%{?dist}
Source: https://github.com/gamag/ka_GE.spell/archive/refs/tags/%{version}.tar.gz#/ka_GE-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 d7ad24a9b84b8e2431ed0f1ffa39a720fbcd967b92d84eb92291d2af9dfd2551
%global source0_file 0.1.tar.gz
# oreon url source checksums end
URL: https://github.com/gamag/ka_GE.spell/
License: MIT AND CC-BY-4.0
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ka)

%description
Georgian hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/0.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d7ad24a9b84b8e2431ed0f1ffa39a720fbcd967b92d84eb92291d2af9dfd2551" || { echo "oreon: Source0 SHA256 mismatch for 0.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n ka_GE.spell-%{version}

%build
# nothing here to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/*.dic dictionaries/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README.md LICENSE.mit
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-5
- Prepare for Oreon 11 (RP1)
