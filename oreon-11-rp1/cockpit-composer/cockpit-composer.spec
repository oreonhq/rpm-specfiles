%global source0_hash 1e954e4f6d0f4d6bb9de4ab9354031656ed63794dc3f1e6a06d81e0785e6af34

Name:           cockpit-composer
Version:        53
Release:        5%{?dist}
Summary:        Composer GUI for use with Cockpit

License:        MIT
URL:            http://weldr.io/
Source0:        https://github.com/osbuild/cockpit-composer/releases/download/53/cockpit-composer-53.tar.gz

BuildArch:      noarch
BuildRequires:  libappstream-glib

Requires:       cockpit
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 8
Requires: osbuild-composer >= 28
%else
Requires: weldr
Suggests: osbuild-composer >= 28
%endif

%description
Composer generates custom images suitable for deploying systems or uploading to
the cloud. It integrates into Cockpit as a frontend for osbuild.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n cockpit-composer

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/cockpit/composer
cp -a public/* %{buildroot}/%{_datadir}/cockpit/composer
mkdir -p %{buildroot}/%{_datadir}/metainfo/
appstream-util validate-relax --nonet public/org.image-builder.cockpit-composer.metainfo.xml
cp -a public/org.image-builder.cockpit-composer.metainfo.xml %{buildroot}/%{_datadir}/metainfo/ 

%files
%doc README.md
%license LICENSE.txt
%{_datadir}/cockpit/composer
%{_datadir}/metainfo/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 53-5
- Prepare for Oreon 11 (RP1)
