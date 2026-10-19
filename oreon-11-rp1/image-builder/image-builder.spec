%global source0_hash e2f3196f505b81fe75f5d436ae2185994fd1ec4a89c65f449b6662df3731d4bd
%global min_osbuild_version 175
%global goipath         github.com/osbuild/image-builder-cli
Version:        53
%gometa
%global common_description %{expand:
A local binary for building customized OS artifacts such as VM images and
OSTree commits. Uses osbuild under the hood.
}
Name:           image-builder
Release:        1%{?dist}
Summary:        An image building executable using osbuild
ExcludeArch:    i686
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-SA-4.0 AND ISC AND MIT AND MPL-2.0 AND Unlicense
URL:            %{gourl}
Source0:        https://github.com/osbuild/image-builder-cli/releases/download/v%{version}/image-builder-cli-%{version}.tar.gz
Requires:   osbuild >= %{min_osbuild_version}
Requires:   osbuild-ostree >= %{min_osbuild_version}
Requires:   osbuild-lvm2 >= %{min_osbuild_version}
Requires:   osbuild-luks2 >= %{min_osbuild_version}
Requires:   osbuild-depsolve-dnf >= %{min_osbuild_version}
# oreon:deps
BuildRequires:  compiler(go-compiler)
BuildRequires:  device-mapper-devel
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel
BuildRequires:  libvirt-devel
BuildRequires:  libxcrypt-devel
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%goprep -k

%build

export GOFLAGS="-buildmode=pie"
export LDFLAGS="${LDFLAGS} -X 'main.version=%{version}'"
%gobuild ${GOTAGS:+-tags=$GOTAGS} -o %{gobuilddir}/bin/image-builder %{goipath}/cmd/image-builder
%install
install -m 0755 -vd                                 %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/image-builder %{buildroot}%{_bindir}/
install -m 0755 -vd                                 %{buildroot}%{_tmpfilesdir}
install -m 0644 -vp data/tmpfiles.d/image-builder.conf %{buildroot}%{_tmpfilesdir}/image-builder.conf
%oreon_autofiles main

%check

export GOFLAGS="-buildmode=pie"
%gocheck
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 53-1
- Prepare for Oreon 11 (RP1)
