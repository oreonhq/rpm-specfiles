%global source0_hash none

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-so
Summary: Somali hunspell dictionaries
Version: 1.0.2
Release: 32%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/2727/2/dict-so.oxt
URL: http://www.opensourcesomalia.org/index.php?page=hingaad-saxe
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-so)

%description
Somali hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T -n %{name}-%{version}
unzip -q %{SOURCE0}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p so_SO.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
so_SO_aliases="so_DJ so_ET so_KE"
for lang in $so_SO_aliases; do
        ln -s so_SO.aff $lang.aff
        ln -s so_SO.dic $lang.dic
done
popd



%files
%doc README_so_SO.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.2-32
- Import
