%global source0_hash c1297f3e7560b40d70b88a4eb0492c098f1cf09f5273645ebf70a703bc6676b9

Name:    shdoc
Version: 1.4
Release: %autorelease
Summary: Documentation generator for bash/zsh/sh for generating documentation in Markdown

License:   MIT
URL:       https://github.com/reconquest/shdoc
Source0:   https://github.com/reconquest/shdoc/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires:  gawk

%description
shdoc is a documentation generator for bash/zsh/sh for generating API
documentation in Markdown from shell scripts source.

shdoc parses annotations in the beginning of a given file and alongside function
definitions, and creates a markdown file with ready to use documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%install
mkdir -p %{buildroot}%{_bindir}
cp -a shdoc %{buildroot}%{_bindir}/shdoc

%files
%{_bindir}/shdoc

%doc README.md
%license LICENSE

%changelog
%autochangelog
