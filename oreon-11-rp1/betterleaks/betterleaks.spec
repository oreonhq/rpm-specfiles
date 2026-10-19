%global source0_hash d59617a0ee7f7763e71b91e333665d35541e51189e2b265fea538ae5f19f6715
%bcond check 1
%global goipath         github.com/betterleaks/betterleaks
Version:                1.9.0
%gometa -L -f
Name:           betterleaks
Release:        1%{?dist}
Summary:        Secrets scanner built for configurability and speed
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
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
A Better Secrets Scanner built for configurability and speed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -p1
tar -xf %{S:1}

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X=github.com/betterleaks/betterleaks/version.Version=%{VERSION}"
%gobuild -o %{gobuilddir}/bin/betterleaks %{goipath}
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
