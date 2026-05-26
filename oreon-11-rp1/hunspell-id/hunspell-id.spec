# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 83d0ab4d72f8d4988e4627bbd70c02624c8d3e603cbdd27f6dcd01b4dfd99e8a
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-id
Summary: Indonesian hunspell dictionaries
%global upstreamid 20220921
# let's continue to use date as version for this package
%global upstreamver 2.3.0
Version: 0.%{upstreamid}
Release: 2%{?dist}
Source: https://github.com/shuLhan/hunspell-id/archive/refs/tags/v%{upstreamver}.tar.gz
URL: https://github.com/shuLhan/hunspell-id
License: LGPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-id)

%description
Indonesian hunspell dictionaries.

%prep
%oreon_verify_sources
%autosetup -n %{name}-%{upstreamver}

%build
# nothing to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%license COPYING
%doc README
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-2
- Prepare for Oreon 11 (RP1)
