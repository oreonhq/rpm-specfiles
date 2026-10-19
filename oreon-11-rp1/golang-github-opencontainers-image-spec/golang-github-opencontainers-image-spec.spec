%global source0_hash fff64f2ae3a11a307227d27ba599f1e56b436301c5a2faedd57907ac97d2ac94
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/opencontainers/image-spec
Version:                1.1.1
%gometa -L -f
%global common_description %{expand:
The OCI Image Format project creates and maintains the software shipping
container image format spec (OCI Image Format).}
%global golicenses      LICENSE
%global godocs          .markdownlint.yml EMERITUS.md GOVERNANCE.md\\\
                        HACKING.md README.md RELEASES.md annotations.md\\\
                        artifacts-guidance.md config.md considerations.md\\\
                        conversion.md descriptor.md image-index.md image-\\\
                        layout.md implementations.md layer.md manifest.md\\\
                        media-types.md project.md spec.md
Name:           golang-github-opencontainers-image-spec
Release:        1%{?dist}
Summary:        OCI Image Format
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/image-spec-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/russross/blackfriday.v1)
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1
sed -i 's|github.com/russross/blackfriday|gopkg.in/russross/blackfriday.v1|' $(find . -iname "*.go" -type f)

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
