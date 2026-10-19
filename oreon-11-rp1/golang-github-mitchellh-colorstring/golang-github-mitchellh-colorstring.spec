%global source0_hash 81153a3df6056eaa280817eb0a762bfd6b59348b01c2680e71e780d50246f846
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mitchellh/colorstring
%global commit          d06e56a500db4d08c33db0b79461e7c9beafca2d
%gometa
%global common_description %{expand:
Colorstring is a Go library for outputting colored strings to a console using a
simple inline syntax in your string to specify the color to print as.
For example, the string [blue]hello [red]world would output the text "hello
world" in two colors. The API of Colorstring allows for easily disabling colors,
adding aliases, etc.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go library for colorizing strings for terminal output
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/colorstring-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
