%global source0_hash 2cbc41662ff6c8df30ff3f6c133d4276db72a6f9b3df7eb942f1a798bcbf3d80
%bcond check 1
%global gomodulesmode GO111MODULE=on
Name:           gum
Version:        2.0.1
Release:        1%{?dist}
ExclusiveArch:  %{golang_arches_future}
Summary:        Tool for glamorous shell scripts
License:        BSD-3-Clause AND MIT AND OFL-1.1
URL:            https://github.com/charmbracelet/gum
Source0:        https://github.com/charmbracelet/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        gum-%{version}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Patch0:         0001-Include-embedded-font-license-in-COPYING-file.patch
# oreon:deps
BuildRequires:  askalono-cli
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
A tool for glamorous shell scripts. Leverage the power of Bubbles and Lip Gloss
in your scripts and aliases without writing any Go code!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1

cd vendor/github.com/alecthomas/chroma/v2
%patch -p 1 -P 0

%build

export GO_LDFLAGS="-X main.Version=v%{version}"
%gobuild -o bin/gum .
%install
%go_vendor_license_install -c %{S:2}
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/gum
install -d -m 0755 %{buildroot}%{_mandir}/man1
./bin/gum man > %{buildroot}%{_mandir}/man1/gum.1
install -d -m 0755 %{buildroot}%{bash_completions_dir}
./bin/gum completion bash > %{buildroot}%{bash_completions_dir}/gum
install -d -m 0755 %{buildroot}%{zsh_completions_dir}
./bin/gum completion zsh > %{buildroot}%{zsh_completions_dir}/_gum
install -d -m 0755 %{buildroot}%{fish_completions_dir}
./bin/gum completion fish > %{buildroot}%{fish_completions_dir}/gum.fish
%oreon_autofiles main

%check

[[ "$(./bin/gum --version)" == "gum version v%{version}" ]] || exit 1
%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck2
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
