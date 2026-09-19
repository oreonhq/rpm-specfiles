%global source0_hash 1fb97c9c90efd739f03dabd8cf5825c2afc95d1f1e0d6cacf62d53a8c540b3df

Name:		colorized-logs
Version:	2.7
Release:	4%{?dist}
Summary:	Tools for logs with ANSI color
License:	MIT
URL:		https://github.com/kilobyte/colorized-logs
Source0:	https://github.com/kilobyte/colorized-logs/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	perl-interpreter

%description
Some tools like gcc, dmesg, grep --color, colordiff, ccze, etc can enhance
their output with color, making reading a lot more pleasant.  The difference
can be as big as between slogging through twenty pages of a build log to
find a failure, and a swift drag of the scroller to do the same within a
second.

Such colored logs can be usually viewed on a terminal or with "less -R";
this package gives you:
 * ansi2html: convert logs to HTML
 * ansi2txt: drop ANSI control codes
 * ttyrec2ansi: drop timing data from ttyrec files
 * pipetty: makes a program think its stdout and stderr are connected to a
   terminal; use as a prefix: "pipetty dmesg|tee"
 * lesstty: pipe a program (as above) to "less -R"

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest -- --output-on-failure

%files
%{_bindir}/ansi2html
%{_bindir}/ansi2txt
%{_bindir}/pipetty
%{_bindir}/lesstty
%{_bindir}/ttyrec2ansi
%{_mandir}/man1/ansi2html.1*
%{_mandir}/man1/ansi2txt.1*
%{_mandir}/man1/pipetty.1*
%{_mandir}/man1/lesstty.1*
%{_mandir}/man1/ttyrec2ansi.1*
%license LICENSE
%doc ChangeLog README

%changelog
%autochangelog
