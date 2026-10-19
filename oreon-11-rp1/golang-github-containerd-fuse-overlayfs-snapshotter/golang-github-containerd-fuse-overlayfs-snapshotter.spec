%global source0_hash 6608130ec613adb3b443d7ed83daa86f3fb62f6670e5f5ff072d850ca587b69e
%bcond check 0
%global goipath         github.com/containerd/fuse-overlayfs-snapshotter
Version:                1.0.4
%gometa
%global goaltipaths     github.com/AkihiroSuda/containerd-fuse-overlayfs
%global godevelheader %{expand:
Provides:     golang-github-akihirosuda-containerd-fuse-overlayfs-devel = %{version}-%{release}
Obsoletes:    golang-github-akihirosuda-containerd-fuse-overlayfs-devel < 1.0.0-3
}
%global common_description %{expand:
Fuse-overlayfs plugin for rootless containerd.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fuse-overlayfs plugin for rootless containerd
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/fuse-overlayfs-snapshotter-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
