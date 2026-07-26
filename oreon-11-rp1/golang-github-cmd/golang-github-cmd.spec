%global source0_hash 757afe093dc84ba591cc04dc63a07a3b24399938e2f0b17979eedb730e41f9d6

%bcond check 0

# https://github.com/go-cmd/cmd
%global debug_package %{nil}

%global goipath         github.com/go-cmd/cmd
Version:                1.4.0

%gometa

%global common_description %{expand:
This package is a small but very useful wrapper around os/exec.Cmd for Linux
and macOS that makes it safe and simple to run external commands in highly
concurrent, asynchronous, real-time applications.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go library wrapper around os/exec.Cmd

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-test/deep)

%description %{common_description}

%gopkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
