%global source0_hash bd97fac716b69493a3160fc5afb04f9a9f34a772086c9f3588bd759ec8dbf63f

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif

Name: hunspell-or
Summary: Odia hunspell dictionaries
Version: 1.0.0
Epoch:   1
Release: 29%{?dist}
License:        GPL-2.0-or-later
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
Source0:        http://anishpatil.fedorapeople.org/or_in.1.0.0.tar.gz
BuildRequires:  hunspell-devel
Requires:       hunspell
Supplements: (hunspell and langpacks-or)
BuildArch: noarch

%description
Odia hunspell dictionaries.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n or_IN

iconv -f ISO-8859-1 -t UTF-8 or_IN/Copyright > or_IN/Copyright.utf8
mv or_IN/Copyright.utf8 or_IN/Copyright

%build


%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
cp -p or_IN/*.dic or_IN/*.aff %{buildroot}%{_datadir}/%{dict_dirname}

%files
%doc or_IN/README
%license or_IN/COPYING or_IN/Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-29
- Prepare for Oreon 11 (RP1)
