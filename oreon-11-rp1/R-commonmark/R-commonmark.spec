%global source0_hash 7f47d7f9f4ff5d1e2a73a69f6e233d2ddbafae97944ddf664a6000aa94936904

Name:           R-commonmark
Version:        %R_rpm_version 2.0.0
Release:        %autorelease
Summary:        High Performance CommonMark and Github Markdown Rendering in R

License:        BSD-2-Clause
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

# Note, this is the GitHub-Flavored Markdown fork, not the one in Fedora.
Provides:       bundled(cmark) = 0.29.0.gfm.13

%description
The CommonMark specification defines a rationalized version of markdown
syntax. This package uses the 'cmark' reference implementation for
converting markdown text into various formats including html, latex and
groff man. In addition it exposes the markdown parse tree in xml format.
Also includes opt-in support for GFM extensions including tables,
autolinks, and strikethrough text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -rf commonmark/tests # unconditional suggest, should be fixed

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
