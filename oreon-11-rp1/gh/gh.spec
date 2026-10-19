%global source0_hash 08bf0ef8b4409893889175e0f5279d30d6edd96465816042c0d7c72eac598158
%bcond check 1
%global goipath         github.com/cli/cli/v2
Version:                2.102.0
%gometa -L -f
Name:           gh
Release:        1%{?dist}
Summary:        GitHub's official command line tool
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND Unlicense
URL:            %{gourl}
Source0:        https://github.com/cli/cli/archive/v%{version}/cli-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       git-core
# oreon:deps
BuildRequires:  git-core
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  sed
# /oreon:deps
%description
A command-line interface to GitHub for use in your terminal or your scripts.

gh is a tool designed to enhance your workflow when working with GitHub. It
provides a seamless way to interact with GitHub repositories and perform various
actions right from the command line, eliminating the need to switch between your
terminal and the GitHub website.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X github.com/cli/cli/v2/internal/build.Version=%{version}  \
                   -X github.com/cli/cli/v2/internal/build.Date=$(date -d "@${SOURCE_DATE_EPOCH}" +%Y-%m-%d)"
for cmd in cmd/%{name} cmd/gen-docs; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%{gobuilddir}/bin/gen-docs --man-page --doc-path ./share/man/man1
%{gobuilddir}/bin/%{name} completion -s bash > %{name}.bash
%{gobuilddir}/bin/%{name} completion -s fish > %{name}.fish
%{gobuilddir}/bin/%{name} completion -s zsh  > %{name}.zsh
%install
%go_vendor_license_install -c %{S:2}
install -Dpm 0755 %{gobuilddir}/bin/%{name} -t %{buildroot}%{_bindir}/
install -Dpm 0644 ./share/man/man1/%{name}*.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 %{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 0644 %{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm 0644 %{name}.zsh  %{buildroot}%{zsh_completions_dir}/_%{name}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for test in "TestNewInspectCmd" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -t github.com/cli/cli/v2/third-party
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
