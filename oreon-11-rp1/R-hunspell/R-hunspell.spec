%global source0_hash 4023df2eef4e081eac52efa1ecccc4b31f7941439ce276f4094b9d5a02787535

Name:           R-hunspell
Version:        %R_rpm_version 3.0.6
Release:        %autorelease
Summary:        High-Performance Stemmer, Tokenizer, and Spell Checker

License:        GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

# Not currently possible to unbundle at the moment.
# https://github.com/ropensci/hunspell/issues/34
Provides: bundled(hunspell) = 1.7.0

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

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
