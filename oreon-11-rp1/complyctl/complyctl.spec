%global source0_hash db8a633a770f76651766fe9472138a15b593885e6f61bc8c822993c68c0b56bf
%global goipath github.com/complytime/complyctl
%global base_url https://%{goipath}
%global app_dir complytime
%global gopath %{_builddir}/go
%global debug_package %{nil}
Name:           complyctl
Version:        1.0.0
Release:        1%{?dist}
Summary:        Tool to perform compliance assessment activities, scaled by plugins
License:        Apache-2.0
URL:            %{base_url}
Source0:        %{base_url}/archive/refs/tags/v%{version}.tar.gz
%gometa -f
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{name} leverages OSCAL to perform compliance assessment activities, using
plugins for each stage of the life-cycle.

%package        openscap-plugin
Summary:        A plugin which extends complyctl capabilities to use OpenSCAP
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       scap-security-guide
%description    openscap-plugin
openscap-plugin is a plugin which extends the complyctl capabilities to use
OpenSCAP. The plugin communicates with complyctl using Remote Procedure Calls,
providing a standard and consistent communication mechanism that allows plugin
developers to use their preferred programming languages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -k

%build

BUILD_DATE_GO=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
%set_build_flags
GO_LD_EXTRAFLAGS="-X %{goipath}/internal/version.version=%{version} \
                  -X %{goipath}/internal/version.gitTreeState=clean \
                  -X %{goipath}/internal/version.commit=%{version} \
                  -X %{goipath}/internal/version.buildDate=${BUILD_DATE_GO}"
export GO111MODULE=on
GO_BUILD_BINDIR=./bin
mkdir -p ${GO_BUILD_BINDIR}
go build -buildmode=pie -o ${GO_BUILD_BINDIR}/ -ldflags="${GO_LD_EXTRAFLAGS}" ./cmd/...
%install
install -d %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_datadir}/%{app_dir}/{plugins,bundles,controls}
install -d -m 0755 %{buildroot}%{_libexecdir}/%{app_dir}/plugins
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{app_dir}/config.d
install -d -m 0755 %{buildroot}%{_mandir}/{man1,man5,man7}
cp -rp docs/samples %{buildroot}%{_datadir}/%{app_dir}
install -p -m 0644 docs/samples/sample-{catalog,profile}.json %{buildroot}%{_datadir}/%{app_dir}/controls
install -p -m 0644 docs/samples/sample-component-definition.json %{buildroot}%{_datadir}/%{app_dir}/bundles
install -p -m 0755 bin/complyctl %{buildroot}%{_bindir}/complyctl
install -p -m 0644 docs/man/complyctl.1 %{buildroot}%{_mandir}/man1/complyctl.1
install -p -m 0755 bin/openscap-plugin %{buildroot}%{_libexecdir}/%{app_dir}/plugins/openscap-plugin
install -p -m 0644 docs/man/complyctl-openscap-plugin.7 %{buildroot}%{_mandir}/man7/complyctl-openscap-plugin.7
install -p -m 0644 docs/man/c2p-openscap-manifest.5 %{buildroot}%{_mandir}/man5/c2p-openscap-manifest.5
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post openscap-plugin

plugin_path=%{_libexecdir}/%{app_dir}/plugins/openscap-plugin
manifest_in=%{_datadir}/%{app_dir}/samples/c2p-openscap-manifest.json
manifest_out=%{_datadir}/%{app_dir}/plugins/c2p-openscap-manifest.json
if [ -f "$plugin_path" ] && [ -f "$manifest_in" ]; then
    checksum=$(sha256sum "$plugin_path" | awk '{ print $1 }')
    version="%{version}"
    sed -e "s|checksum_placeholder|$checksum|" \
        -e "s|version_placeholder|$version|" \
        "$manifest_in" > "$manifest_out"
fi
%check

go test -mod=vendor -race -v ./...
%files -f %{oreon_filedir}/main.list
%files -n complyctl-openscap-plugin -f %{oreon_filedir}/complyctl-openscap-plugin.list

%changelog

%autochangelog
