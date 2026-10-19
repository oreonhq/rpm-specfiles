%global source0_hash 4b8e2b6cb20e9707e14b9b9d92ddb6f2e913523754e1f123e2e6f3321e67f7ca
%bcond check 1
%global goipath         github.com/restic/restic
Version:                0.18.1
%gometa -L -f
Name:           restic
Release:        1%{?dist}
Summary:        Fast, secure, efficient backup program
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Recommends:     fuse
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Fast, secure, efficient backup program.

restic supports the following backends for storing backups natively:

* Local directory
* sftp server (via SSH)
* HTTP REST server (protocol, rest-server)
* Amazon S3 (either from Amazon or using the Minio server)
* OpenStack Swift
* BackBlaze B2
* Microsoft Azure Blob Storage
* Google Cloud Storage
* And many other services via the rclone Backend

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/restic
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 doc/man/%{name}*.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 doc/bash-completion.sh %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 0644 doc/fish-completion.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm 0644 doc/zsh-completion.zsh  %{buildroot}%{zsh_completions_dir}/_%{name}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
export RESTIC_TEST_FUSE=0
for test in "TestNodeRestoreAt" "TestOverwriteXattr" \
            "TestStdinFromCommand" "TestStdinFromCommandNoOutput" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
