%global source0_hash 18df6f3c09157021366b8c702b5badba405d37dbb42f132353eb50c1b0d3f464
%bcond check 1
%global gomodulesmode GO111MODULE=on
Name:           glow
Version:        3.0.0
Release:        1%{?dist}
ExclusiveArch:  %{golang_arches_future}
Summary:        Terminal based markdown reader
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND OFL-1.1
URL:            https://github.com/charmbracelet/glow
Source0:        https://github.com/charmbracelet/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        glow-%{version}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  askalono-cli
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Glow is a terminal based markdown reader designed from the ground up to bring
out the beauty—and power—of the CLI.  Use it to discover markdown files, read
documentation directly on the command line.  Glow will find local markdown
files in subdirectories or a local Git repository.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export GO_LDFLAGS="-X main.Version=v%{version}"
%gobuild -o bin/glow .
%install
%go_vendor_license_install -c %{S:2}
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/glow
install -d -m 0755 %{buildroot}%{_mandir}/man1
./bin/glow man > %{buildroot}%{_mandir}/man1/glow.1
install -d -m 0755 %{buildroot}%{bash_completions_dir}
./bin/glow completion bash > %{buildroot}%{bash_completions_dir}/glow
install -d -m 0755 %{buildroot}%{zsh_completions_dir}
./bin/glow completion zsh > %{buildroot}%{zsh_completions_dir}/_glow
install -d -m 0755 %{buildroot}%{fish_completions_dir}
./bin/glow completion fish > %{buildroot}%{fish_completions_dir}/glow.fish
%oreon_autofiles main

%check

[[ "$(./bin/glow --version)" == "glow version v%{version}" ]] || exit 1
%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck2
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
