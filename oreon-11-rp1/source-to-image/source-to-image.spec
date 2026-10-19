%global source0_hash 08880e67770a5f16d39af96570a86687f2d7a0fc88205e7507770909860ab549
%bcond check 1
%bcond btrfs %{undefined rhel}
%global goipath         github.com/openshift/source-to-image
Version:                1.5.1
%gometa -L -f
Name:           source-to-image
Release:        1%{?dist}
Summary:        A tool for building artifacts from source and injecting into container images
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
%if %{with btrfs}
%endif
Requires:      git-core
Requires:      tar
Provides:      s2i = %{version}-%{release}
# oreon:deps
BuildRequires:  btrfs-progs-devel
BuildRequires:  device-mapper-devel
BuildRequires:  git-core
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description
Source-to-Image (S2I) is a toolkit and workflow for building reproducible 
container images from source code. S2I produces ready-to-run images by 
injecting source code into a container image and letting the container prepare 
that source code for execution. By creating self-assembling builder images, 
you can version and control your build environments exactly like you use 
container images to version your runtime environments.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -p1
tar -xf %{S:1}

%build

%global gomodulesmode GO111MODULE=on
%if %{without btrfs}
export GO_BUILDTAGS="exclude_graphdriver_btrfs"
%endif
export GO_LDFLAGS="-X %{goipath}/pkg/version.versionFromGit=v%{version}"
for cmd in cmd/s2i ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%{gobuilddir}/bin/s2i completion bash > s2i.bash
%{gobuilddir}/bin/s2i completion zsh > s2i.zsh
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd          %{buildroot}%{bash_completions_dir}
install -m 0644 -vp s2i.bash %{buildroot}%{bash_completions_dir}/s2i
install -m 0755 -vd          %{buildroot}%{zsh_completions_dir}
install -m 0644 -vp s2i.zsh  %{buildroot}%{zsh_completions_dir}/s2i
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{without btrfs}
export GO_BUILDTAGS="exclude_graphdriver_btrfs"
%endif
%if %{with check}
%gocheck2 -d pkg/scm/git
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
