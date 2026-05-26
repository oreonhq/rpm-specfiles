# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 b3322235b821a3db6796a277c378f6c8d40614ca076673d9de34a8b3c35e3e73
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif

Name: hunspell-pa
Summary: Punjabi hunspell dictionaries
Version: 1.0.0
Release: 29%{?dist}
Epoch: 1
Source: http://anishpatil.fedorapeople.org/pa_in.%{version}.tar.gz
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-pa)

%description
Punjabi hunspell dictionaries.

%prep
%oreon_verify_sources
%autosetup -c -n pa_IN
iconv -f ISO-8859-1 -t UTF-8 pa_IN/Copyright > pa_IN/Copyright.utf8
mv pa_IN/Copyright.utf8 pa_IN/Copyright

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p pa_IN/*.dic pa_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc pa_IN/README
%license pa_IN/COPYING pa_IN/Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-29
- Prepare for Oreon 11 (RP1)
