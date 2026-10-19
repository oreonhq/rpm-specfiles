%global source0_hash bd97fac716b69493a3160fc5afb04f9a9f34a772086c9f3588bd759ec8dbf63f
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon} >= 11
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-or
Summary:        Odia hunspell dictionaries
Version: 2.0.0
Epoch:   1
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
Requires:       hunspell
Supplements: (hunspell and langpacks-or)
BuildArch: noarch
Source0:        https://anishpatil.fedorapeople.org/or_in.1.0.0.tar.gz
# oreon:deps
BuildRequires:  hunspell-devel
# /oreon:deps
%description
Odia hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n or_IN
iconv -f ISO-8859-1 -t UTF-8 or_IN/Copyright > or_IN/Copyright.utf8
mv or_IN/Copyright.utf8 or_IN/Copyright

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
cp -p or_IN/*.dic or_IN/*.aff %{buildroot}%{_datadir}/%{dict_dirname}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-29
- Prepare for Oreon 11 (RP1)
