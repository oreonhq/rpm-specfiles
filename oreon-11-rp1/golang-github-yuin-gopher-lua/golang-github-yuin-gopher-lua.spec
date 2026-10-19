%global source0_hash adb4368b10c7160e41b44ec855354ec890cd3a6b712e7dafa2c6b84d10f98119
%bcond check 0
%global goipath         github.com/yuin/gopher-lua
%global commit          f4c35e4016d9d8580b007ebaeb68ecd8e0b09f1c
%gometa
%global common_description %{expand:
GopherLua is a Lua5.1 VM and compiler written in Go. GopherLua has a same goal
with Lua: Be a scripting language with extensible semantics . It provides Go
APIs that allow you to easily embed a scripting language to your Go host
programs.}
%global golicenses      LICENSE
%global godocs          README.rst
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        VM and compiler for Lua in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gopher-lua-%{commit}.tar.gz
Patch0:         0001-Convert-int-to-string-using-rune-in-lexer.go.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/chzyer/readline)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

%build

for cmd in cmd/* ; do
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
