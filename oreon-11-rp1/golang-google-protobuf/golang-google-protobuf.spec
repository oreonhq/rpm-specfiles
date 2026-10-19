%global source0_hash 96d670e9bae145ff2dd0f48a3693edb1f45ec3ee56d5f50a5f01cc7e060314bc
%bcond check 0
%global goipath         google.golang.org/protobuf
%global forgeurl        https://github.com/protocolbuffers/protobuf-go
Version:                1.31.0
%gometa -f
%global common_description %{expand:
Go support for Google's protocol buffers.}
%global golicenses      LICENSE PATENTS
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go support for Google's protocol buffers
%global godevelheader   %{expand:
Obsoletes:              compat-golang-github-protobuf-devel < 1.31.0-3
}
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/protobuf-go-%{version}.tar.gz
Requires:       protobuf
Provides:       protoc-gen-go = %{version}-%{release}
Provides:       golang(%{goipath}/protoc-gen-go) = %{version}-%{release}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  protobuf-compiler
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
