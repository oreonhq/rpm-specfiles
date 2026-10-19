%global source0_hash fec94d3c8b14cadad162b5707f4d706dcd18f14a67b574392dfabcfb6be6fc46
%bcond check 0
%bcond_without bundled
%if %{with bundled}
%global gomodulesmode   GO111MODULE=on
%endif
%global goipath         github.com/containers/prometheus-podman-exporter
Version:                1.20.0
%gometa -f
%global goname prometheus-podman-exporter
%global common_description %{expand:
Prometheus exporter for podman environments exposing containers, pods, images,
volumes and networks information.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md MAINTAINERS.md\\\
                        README.md SECURITY.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Prometheus exporter for podman environment
License:        Apache-2.0 AND MPL-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT AND Unlicense AND CC-BY-SA-4.0 AND ISC
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  glibc-devel
BuildRequires:  glibc-static
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libassuan)
# /oreon:deps
%description %{common_description}

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
export LDFLAGS="-X %{goipath}/cmd.buildVersion=%{version} -X %{goipath}/cmd.buildRevision=%{release} -X %{goipath}/cmd.buildBranch=main"
%gobuild -o %{gobuilddir}/bin/prometheus-podman-exporter %{goipath}
%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_unitdir}
install -m 0755 -vd                     %{buildroot}%{_userunitdir}
install -m 0755 -vd                     %{buildroot}%{_sysconfdir}/sysconfig/
install -m 0644 -vp ./contrib/systemd/system/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m 0644 -vp ./contrib/systemd/system/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -m 0644 -vp ./contrib/systemd/user/%{name}.service %{buildroot}%{_userunitdir}/%{name}.service
%oreon_autofiles main

%post

%systemd_user_post %{name}.service
%systemd_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%systemd_preun %{name}.service
%if %{with check}
%check

%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
