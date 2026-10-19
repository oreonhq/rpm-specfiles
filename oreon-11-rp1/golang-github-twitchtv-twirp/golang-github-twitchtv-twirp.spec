%global source0_hash 0d186367d002da71cbb1e94341037208658ada2367fad43661d8f3a4182ed308
%bcond check 0
%global goipath         github.com/twitchtv/twirp
Version:                8.1.0
%gometa
%global common_description %{expand:
A simple RPC framework with protobuf service definitions.}
%global golicenses      LICENSE NOTICE
%global godocs          docs example CONTRIBUTING.md PROTOCOL.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A simple RPC framework with protobuf service definitions
License:        ASL 2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/twirp-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(google.golang.org/protobuf/encoding/protojson)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  golang(google.golang.org/protobuf/types/descriptorpb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/emptypb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/wrapperspb)
BuildRequires:  golang(google.golang.org/protobuf/types/pluginpb)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
# remove vendored tools
rm -r _tools

%build

for cmd in protoc-gen-twirp clientcompat clientcompat/gocompat; do
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
