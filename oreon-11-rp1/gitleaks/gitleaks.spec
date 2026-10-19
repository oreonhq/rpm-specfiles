%global source0_hash e90fb266d75837e75894c778bf594ab8e2787f12dce5a62651f21b893eaf9abb
%bcond check 1
%global goipath         github.com/zricethezav/gitleaks/v8
Version:                8.30.1
%gometa -L -f
Name:           gitleaks
Release:        1%{?dist}
Summary:        Scan git repos (or files) for secrets using regex and entropy
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://github.com/zricethezav/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       git-core
# oreon:deps
BuildRequires:  git-core
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Scan git repos (or files) for secrets using regex and entropy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

export GO_LDFLAGS="-X=github.com/zricethezav/gitleaks/v8/version.Version=%{VERSION}"
%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/gitleaks %{goipath}
%{gobuilddir}/bin/%{name} completion bash > %{name}.bash
%{gobuilddir}/bin/%{name} completion fish > %{name}.fish
%{gobuilddir}/bin/%{name} completion zsh  > %{name}.zsh
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
