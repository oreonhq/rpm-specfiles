%global source0_hash 210b691917864c0413134efeaa426139c9feefb3d039462a541ebddc6cae74e1
%bcond check 0
%bcond_without bundled
%if %{with bundled}
%global gomodulesmode   GO111MODULE=on
%endif
%global goipath github.com/containers/podman-tui
Version: 1.11.1
%gometa
%global goname podman-tui
%global common_description %{expand:
%{goname} is a terminal user interface for Podman.
%{goname} is using podman.socket service to communicate with podman environment
and SSH to connect to remote podman machines.
}
%global golicenses LICENSE
%global godocs CODE-OF-CONDUCT.md CONTRIBUTING.md README.md
%global godevelheader %{expand:
Requires:  %{name} = %{version}-%{release}
}
Name: %{goname}
Release:        1%{?dist}
Summary:        Podman Terminal User Interface
License: Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL: %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:         vendor-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel
BuildRequires:  glibc-static
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  make
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep %{?with_bundledc:-k}
%if %{with bundled}
%setup -q -T -D -a 1 -n %{name}-%{version}
%endif

%if %{without bundled}
%build

%if %{with bundled}
export GOFLAGS="-mod=vendor"
%endif
export BUILDTAGS="exclude_graphdriver_devicemapper exclude_graphdriver_btrfs btrfs_noversion containers_image_openpgp remote"
export CGO_LDFLAGS="${CGO_LDFLAGS} -Wl,--allow-multiple-definition"
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}
%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
