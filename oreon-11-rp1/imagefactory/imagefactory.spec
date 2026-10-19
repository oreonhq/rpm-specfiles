%global source0_hash 2de22444da921fda7511680d569c9a936ec1147bf0124ac644cd95f58d5774f8
Name: imagefactory
Version: 1.1.16
Release:        1%{?dist}
Summary:        System image generation tool
License: Apache-2.0
URL: https://github.com/redhat-imaging/imagefactory
Source0:        https://github.com/redhat-imaging/imagefactory/archive/imagefactory-%{version}-1.tar.gz
Patch0: imagefactory-1.1.14-utf8-config-id.patch
Patch1: container-github-pr434.patch
Patch2: 0001-ApplicationConfiguration.py-drop-encoding-from-json..patch
Patch3: imagefactory-Docker.py-Pass-the-use_ino-option-to-fix-hardlnks.patch
Patch4: 0001-TinMan.py-adjust-to-oz-generate_diskimage-size-unit-.patch
Patch5: 0001-bottle-fix-for-Python-3.12-backport-CVE-2022-31799-f.patch
Patch6: 0002-Python-3.12-adjust-for-removal-of-SafeConfigParser.patch
BuildArch: noarch
Requires: python3-pycurl
Requires: python3-libguestfs
Requires: python3-zope-interface
Requires: python3-libxml2
Requires: python3-httplib2
Requires: python3-cherrypy
Requires: python3-oauth2
Requires: python3-libs
Requires: python3-setuptools
Requires: oz
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: bundled(python-bottle)
Provides: imagefactory-plugin-api = 1.0
# oreon:deps
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-units
# /oreon:deps
%description
imagefactory allows the creation of system images for multiple virtualization
and cloud providers from a single template definition. See
https://github.com/redhat-imaging/imagefactory for more information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir imagefactory-imagefactory-%{version}-1
%oreon_prep
%build

%py3_build
%install
%py3_install
install -d %{buildroot}/%{_sysconfdir}/imagefactory/jeos_images
install -d %{buildroot}/%{_localstatedir}/lib/imagefactory/images
install -d %{buildroot}/%{_sysconfdir}/imagefactory/plugins.d
install -d %{buildroot}/%{_sysconfdir}/logrotate.d
install -m0600 conf/sysconfig/imagefactoryd %{buildroot}/%{_sysconfdir}/sysconfig/imagefactoryd
install -m0600 conf/logrotate.d/imagefactoryd %{buildroot}/%{_sysconfdir}/logrotate.d/imagefactoryd
rm -f %{buildroot}/%{_initddir}/imagefactoryd
%oreon_autofiles main

%post

%systemd_post imagefactoryd.service
%preun

%systemd_preun imagefactoryd.service
%postun

%systemd_postun imagefactoryd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
