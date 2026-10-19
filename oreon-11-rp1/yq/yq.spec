%global source0_hash 48ef09b9ffdb80f26ee516fa2fc83f713c1b49f503cedef79a96435509d456af
%bcond check 1
%global goipath         github.com/mikefarah/yq/v4
Version:                4.47.1
%gometa -L -f
Name:           yq
Release:        1%{?dist}
Summary:        Yq is a portable command-line YAML, JSON, XML, CSV, TOML  and properties processor
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://github.com/mikefarah/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Yq is a portable command-line YAML, JSON, XML, CSV, TOML  and properties
processor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/yq %{goipath}
%{gobuilddir}/bin/%{name} shell-completion bash > %{name}.bash
%{gobuilddir}/bin/%{name} shell-completion fish > %{name}.fish
%{gobuilddir}/bin/%{name} shell-completion zsh  > %{name}.zsh
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
