%global source0_hash 444225a2edacb05ebfc656bf6cabb77d1a962acf1dbe329d0ee5ae3661fe4912
%ifnarch %{arm} %{ix86}
%bcond check 0
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(golang.org/x/sys/unix\\)$
%global goipath             go.starlark.net
%global forgeurl            https://github.com/google/starlark-go
%global commit              0d7263928a74a8d4cf6e23b648bace6925b65dbb
%gometa
%global common_description %{expand:
Starlark is a dialect of Python intended for use as a configuration language.
Like Python, it is an untyped dynamic language with high-level data types,
first-class functions with lexical scope, and garbage collection. Unlike
CPython, independent Starlark threads execute in parallel, so Starlark
workloads scale well on parallel machines. Starlark is a small and simple
language with a familiar and highly readable syntax. You can use it as an
expressive notation for structured data, defining functions to eliminate
repetition, or you can use it to add scripting capabilities to an existing
application.}
%global golicenses          LICENSE
%global godocs              *.md
%global gosupfiles      ${star[@]}
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Dialect of Python intended for use as a configuration language
License:        LicenseRef-Callaway-BSD AND Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/starlark-go-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/chzyer/readline)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(google.golang.org/protobuf/encoding/protojson)
BuildRequires:  golang(google.golang.org/protobuf/encoding/prototext)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protodesc)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoregistry)
BuildRequires:  golang(google.golang.org/protobuf/types/descriptorpb)
BuildRequires:  golang(google.golang.org/protobuf/types/dynamicpb)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%go_generate_buildrequires

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
mapfile -t star <<< $(find . -name "*.star" -type f)
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
