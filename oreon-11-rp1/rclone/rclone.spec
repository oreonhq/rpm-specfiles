%global source0_hash 91c777ce0bf41caa5de9aeaeae37310f9310bd7b12b5eee7337f57cbaae5830c
%bcond check 1
%global goipath         github.com/rclone/rclone
Version:                1.73.0
%gometa -L -f
Name:           rclone
Release:        1%{?dist}
Summary:        Rsync for cloud storage
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND LGPL-3.0-only AND MIT AND MPL-2.0 AND (Apache-2.0 OR MIT)
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
"rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive,
Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex
Files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export LDFLAGS="-X github.com/rclone/rclone/fs.Version=v%{version}"
%gobuild -o %{gobuilddir}/bin/rclone %{goipath}
%{gobuilddir}/bin/%{name} completion bash - > %{name}.bash
%{gobuilddir}/bin/%{name} completion fish - > %{name}.fish
%{gobuilddir}/bin/%{name} completion zsh  - > %{name}.zsh
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 ./rclone.1 %{buildroot}%{_mandir}/man1/rclone.1
install -Dpm 0644 %{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 0644 %{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm 0644 %{name}.zsh  %{buildroot}%{zsh_completions_dir}/_%{name}
install -m 0755 -vd                     %{buildroot}%{_sbindir}
ln -rs %{buildroot}%{_bindir}/rclone %{buildroot}%{_sbindir}/mount.rclone
ln -rs %{buildroot}%{_bindir}/rclone %{buildroot}%{_bindir}/rclonefs
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for test in "TestZenodoRemote" "TestMetadata" "TestIntegration" "TestFTP" \
            "TestS3" "TestSftp" "TestWebDav" "TestMetadataMapper" \
            "TestLogger" "TestStatsGroupOperations" "TestRcDu" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -d backend/ftp \
         -d backend/hdfs \
         -d backend/sftp \
         -d backend/smb \
         -d backend/webdav \
         -d cmd/mount \
         -d cmd/mount2 \
         -d cmd/selfupdate \
         -d cmd/serve/docker \
         -d fs/rc/webgui
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
