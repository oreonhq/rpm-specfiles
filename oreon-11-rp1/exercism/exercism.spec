%global source0_hash 386cee0117c42a0ead45b6f636f96c2fc20cc5f64f802fcda93c7a0778330f3c
%bcond check 1
%global goipath         github.com/exercism/cli
Version:                3.5.8
%gometa -L -f
Name:           exercism
Release:        1%{?dist}
Summary:        Exercism command-line interface
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cli-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Patch:          0001-Disable-self-update.patch
Patch:          0002-Fix-non-constant-format-strings.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description
Exercism provides a way to do the problems on https://exercism.io.

This CLI ships as a binary with no additional run-time requirements. This means 
that if you're doing the Haskell problems on exercism you don't need a working 
Python or Ruby environment simply to fetch and submit exercises.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1 -q

%build

%global gomodulesmode GO111MODULE=on
for cmd in exercism; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -Dpm0644 shell/exercism_completion.bash %{buildroot}%{_datadir}/bash-completion/completions/exercism
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
install -Dpm0644 shell/exercism.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/exercism.fish
install -d %{buildroot}%{_datadir}/zsh/site-functions
install -Dpm0644 shell/exercism_completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_exercism
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
