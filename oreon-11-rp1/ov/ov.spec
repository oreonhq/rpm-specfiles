%global source0_hash 740d018007e7da96787c057261e5a239513754102d1ad34d196e028221de0797
%bcond check 1
%global goipath         github.com/noborus/ov
Version:                0.51.1
%gometa -L -f
Name:           ov
Release:        1%{?dist}
Summary:        Feature-rich terminal-based text viewer
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Feature-rich terminal-based text viewer. It is a so-called terminal pager.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/ov %{goipath}
%{gobuilddir}/bin/%{name} --completion bash > %{name}.bash
%{gobuilddir}/bin/%{name} --completion fish > %{name}.fish
%{gobuilddir}/bin/%{name} --completion zsh  > %{name}.zsh
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 %{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 0644 %{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm 0644 %{name}.zsh  %{buildroot}%{zsh_completions_dir}/_%{name}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
