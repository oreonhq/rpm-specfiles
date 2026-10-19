%global source0_hash 9c06b67eaf33993f8ca33204e60042c8fdf4dc6d203d4bdd5e6aef8790f1769c
%bcond check 1
%global goipath         github.com/checkpoint-restore/checkpointctl
Version:                1.4.1
%gometa -L -f
Name:           checkpointctl
Epoch:          1
Release:        1%{?dist}
Summary:        A command-line tool for in-depth analysis of container checkpoints
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  python3-click
# /oreon:deps
%description
The checkpointctl command can be used for in-depth analysis of
container checkpoints created with Podman and Kubernetes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/checkpointctl %{goipath}
%{gobuilddir}/bin/%{name} completion bash > %{name}.bash
%{gobuilddir}/bin/%{name} completion fish > %{name}.fish
%{gobuilddir}/bin/%{name} completion zsh  > %{name}.zsh
pushd docs
cat > footer.adoc <<'EOF'
The CRIU team
v%{version}
:doctype: manpage
:mansource: checkpointctl
:manversion: v%{version}
:manmanual: CHECKPOINTCTL Manual
EOF
for src in checkpointctl.adoc checkpointctl-inspect.adoc checkpointctl-memparse.adoc checkpointctl-show.adoc; do
    out="${src%.adoc}.1"
    asciidoctor -b manpage -d manpage -o "$out" "$src"
done
popd
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 %{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 0644 %{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm 0644 %{name}.zsh  %{buildroot}%{zsh_completions_dir}/_%{name}
install -Dpm 0644 ./docs/%{name}*.1 -t %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
