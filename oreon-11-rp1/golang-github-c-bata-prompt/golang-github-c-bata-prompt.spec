%global source0_hash 6b249608d52ab66d33d85dcc5ec0a4f5f74f63ec6f22f8cfb12c96cb3a9b05cf
%bcond check 0
%global goipath         github.com/c-bata/go-prompt
Version:                0.2.6
%gometa
%global common_description %{expand:
A library for building powerful interactive prompts inspired by
python-prompt-toolkit, making it easier to build cross-platform command line
tools using Go.}
%global golicenses      LICENSE
%global godocs          _example CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Building powerful interactive prompts in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-prompt-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(github.com/pkg/term/termios)
BuildRequires:  golang(golang.org/x/sys/unix)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in _tools/sigwinch _tools/vt100_debug _tools/complete_file; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
