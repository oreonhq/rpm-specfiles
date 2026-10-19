%global source0_hash 82be23c4cab66f0911a6ff4ed225a0abd9a05c51475f0098b8d8d0ad1490631a
%bcond check 1
%global goipath         github.com/cilium/ebpf
Version:                0.22.0
%gometa
%global common_description %{expand:
Ebpf-go is a pure-Go library to read, modify and load eBPF programs and attach
them to various hooks in the Linux kernel.}
%global golicenses      LICENSE
%global godocs          examples ARCHITECTURE.md CODE_OF_CONDUCT.md\\\
                        CONTRIBUTING.md MAINTAINERS.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        EBPF Library for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/ebpf-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/bpf2go %{goipath}/cmd/bpf2go
%install
%gopkginstall
install -m 0755 -vd                          %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/bpf2go %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
