%global source0_hash 325b28bd5e8da316e319361f2dd8e3cc74fcd55724fc8ad4b2a73c21b2903bd8

# https://github.com/vrothberg/vgrep
%global goipath         github.com/vrothberg/vgrep
Version:                2.8.0

%gometa -f

%global common_description %{expand:
vgrep is a pager for grep, git-grep, ripgrep and similar grep implementations,
and allows for opening the indexed file locations in a user-specified editor
such as vim or emacs. vgrep is inspired by the ancient cgvg scripts but
extended to perform further operations such as listing statistics of files and
directory trees or showing the context lines before and after the matches.}

%global golicenses      LICENSE
%global godocs          README.md

%bcond check 0

Name:           vgrep
Release:        %autorelease
Summary:        User-friendly pager for grep
License:        GPL-3.0-only
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  go-md2man

%description %{common_description}

%gopkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
export LDFLAGS="-X main.version=%{version} "
%gobuild -o %{gobuilddir}/bin/vgrep %{goipath}
go-md2man -in docs/vgrep.1.md -out docs/vgrep.1

%install
%gopkginstall
install -D -p -m 0755 %{gobuilddir}/bin/vgrep %{buildroot}%{_bindir}/vgrep
install -D -p -m 0644 docs/vgrep.1 %{buildroot}%{_mandir}/man1/vgrep.1

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/vgrep
%{_mandir}/man1/vgrep.1*

%gopkgfiles

%changelog
%autochangelog
