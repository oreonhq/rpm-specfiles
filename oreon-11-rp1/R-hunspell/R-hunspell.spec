%global source0_hash 4023df2eef4e081eac52efa1ecccc4b31f7941439ce276f4094b9d5a02787535
Name:           R-hunspell
Version:        %R_rpm_version 3.0.6
Release:        1%{?dist}
Summary:        High-Performance Stemmer, Tokenizer, and Spell Checker
License:        GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=hunspell&version=%{version}#/hunspell_%{version}.tar.gz
ExcludeArch:    %{ix86}
Provides: bundled(hunspell) = 1.7.0
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Low level spell checker and morphological analyzer based on the famous
'hunspell' library <https://hunspell.github.io>. The package can analyze or
check individual words as well as parse text, latex, html or xml documents.
For a more user-friendly interface use the 'spelling' package which builds
on this package to automate checking of files, documentation and vignettes
in all common formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f hunspell/tests/spelling.R # dev stuff

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
