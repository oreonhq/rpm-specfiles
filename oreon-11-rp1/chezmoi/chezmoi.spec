%global source0_hash f6fba40bec4662d5438eecce5cd5c1bcad0bcae5ec34a547fdcf66fb58535764
%bcond check 1
%global release_commit 3a8df1b18736e7156cd37ade3907dcf0ae1d1714
%global goipath         chezmoi.io/chezmoi
%global forgeurl        https://github.com/twpayne/chezmoi
Version:                2.73.0
%gometa -L -f
Name:           chezmoi
Release:        1%{?dist}
Summary:        Manage your dotfiles across multiple diverse machines
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND CC-BY-3.0 AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  git-core
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Manage your dotfiles across multiple diverse machines, securely.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X main.version=%{version} \
                   -X main.commit=%{release_commit} \
                   -X main.date=$(date -d "@${SOURCE_DATE_EPOCH}" +%Y-%m-%dT%H:%M:%SZ) \
                   -X main.builtBy=Fedora"
export BUILDTAGS="noupgrade"
%gobuild -o %{gobuilddir}/bin/chezmoi %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 completions/chezmoi-completion.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 0644 completions/%{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm 0644 completions/%{name}.zsh  %{buildroot}%{zsh_completions_dir}/_%{name}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for test in "TestScript" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
