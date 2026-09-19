%global source0_hash 1a9f680ffe563abdaa91add6ebf5e6c0ecbe57f0d39687bcb272ff2a987c33bb

Name:           R-R.rsp
Version:        %R_rpm_version 0.46.0
Release:        %autorelease
Summary:        Dynamic Generation of Scientific Reports

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
The RSP markup language makes any text-based document come alive.  RSP provides
a powerful markup for controlling the content and output of LaTeX, HTML,
Markdown, AsciiDoc, Sweave and knitr documents (and more), e.g. 'Today's date
is <%=Sys.Date()%>'.  Contrary to many other literate programming languages,
with RSP it is straightforward to loop over mixtures of code and text sections,
e.g. in month-by-month summaries.  RSP has also several preprocessing
directives for incorporating static and dynamic contents of external files
(local or online) among other things.  Functions rstring() and rcat() make it
easy to process RSP strings, rsource() sources an RSP file as it was an R
script, while rfile() compiles it (even online) into its final output format,
e.g. rfile('report.tex.rsp') generates 'report.pdf' and rfile('report.md.rsp')
generates 'report.html'.  RSP is ideal for self-contained scientific reports
and R package vignettes.  It's easy to use - if you know how to write an R
script, you'll be up and running within minutes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f R.rsp/tests/multi,selfcontained.R # unconditional suggest, should be fixed

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
