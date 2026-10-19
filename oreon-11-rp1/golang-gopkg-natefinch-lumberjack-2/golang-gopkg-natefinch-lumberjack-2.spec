%global source0_hash 5817941b45096eb70b8114d7a4bf392ea47c4fe8030ff383ca54c67dfa0617bd
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/natefinch/lumberjack.v2
%global forgeurl        https://github.com/natefinch/lumberjack
Version:                2.0.0
%gometa
%global common_description %{expand:
Lumberjack is a Go package for writing logs to rolling files.
Lumberjack is intended to be one part of a logging infrastructure. It is not
an all-in-one solution, but instead is a pluggable component at the bottom of
the logging stack that simply controls the files to which logs are written.
Lumberjack plays well with any logging package that can write to an io.Writer,
including the standard library's log package.
Lumberjack assumes that only one process is writing to the output files. Using
the same lumberjack configuration from multiple processes on the same machine
will result in improper behavior.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Epoch:          1
Release:        1%{?dist}
Summary:        Rolling logger for Go
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/lumberjack-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(gopkg.in/yaml.v2)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
