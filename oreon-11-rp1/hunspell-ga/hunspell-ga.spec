# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8988e1d46b8f59e70bc2f86aec0055cdd0374661eeffe379835e07804f797f7f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ga
Summary: Irish hunspell dictionaries
Version: 5.1
Release: 10%{?dist}
Source: https://github.com/kscanne/gaelspell/releases/download/v%{version}/hunspell-ga-%{version}.zip
URL: https://cadhan.com/gaelspell/
License: GPL-2.0-or-later
BuildArch: noarch
BuildRequires: make
BuildRequires: hunspell-devel

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ga)

%description
Irish hunspell dictionaries.

%prep
%oreon_verify_sources
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ga_IE.dic ga_IE.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_ga_IE.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1-10
- Prepare for Oreon 11 (RP1)
