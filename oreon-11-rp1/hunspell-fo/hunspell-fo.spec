%global source0_hash 17074d00c490fa80b8e881e350675b6fb45a000da0d20c621bba67e3511a66b7

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fo
Summary: Faroese hunspell dictionaries
Version: 0.4.2
Release: 27%{?dist}
URL: http://fo.speling.org/
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-fo)

Source0:        https://github.com/wooorm/dictionaries/archive/refs/heads/main.tar.gz#/dictionaries-main.tar.gz

%description
Faroese hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n dictionaries-main

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/fo/index.aff %{buildroot}%{_datadir}/%{dict_dirname}/fo_FO.aff
install -pm 0644 dictionaries/fo/index.dic %{buildroot}%{_datadir}/%{dict_dirname}/fo_FO.dic

%files
%doc dictionaries/fo/readme.md
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.2-27
- Import
