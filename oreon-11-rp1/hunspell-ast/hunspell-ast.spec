%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ast
Summary: Asturian hunspell dictionaries
Epoch: 1
Version: 2.0
Release: 18%{?dist}
Source: https://extensions.libreoffice.org/extensions/correutor-ortograficu-dasturianu/2.0/@@download/file/ort_ast_20190216_1129.oxt
URL: http://softastur.org/
License: GPL-1.0-or-later OR LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ast)

%description
Asturian hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c

%build
chmod -x dictionaries/*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/ast.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ast_ES.aff
cp -p dictionaries/ast.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ast_ES.dic


%files
%doc licenses/license-ast.txt licenses/license-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:2.0-18
- Import
