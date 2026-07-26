%global source0_hash 2de22444da921fda7511680d569c9a936ec1147bf0124ac644cd95f58d5774f8

Name: imagefactory
Version: 1.1.16
Release: 21%{?dist}
Summary: System image generation tool
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/redhat-imaging/imagefactory

Source0: https://github.com/redhat-imaging/imagefactory/archive/imagefactory-%{version}-1.tar.gz
Patch0: imagefactory-1.1.14-utf8-config-id.patch
# https://github.com/redhat-imaging/imagefactory/pull/434
Patch1: container-github-pr434.patch
# https://github.com/redhat-imaging/imagefactory/pull/438
Patch2: 0001-ApplicationConfiguration.py-drop-encoding-from-json..patch
# https://github.com/redhat-imaging/imagefactory/issues/412
# https://bugzilla.redhat.com/show_bug.cgi?id=2245066
# https://github.com/redhat-imaging/imagefactory/pull/455
Patch3: imagefactory-Docker.py-Pass-the-use_ino-option-to-fix-hardlnks.patch
# https://github.com/redhat-imaging/imagefactory/pull/458
# this goes along with https://github.com/clalancette/oz/pull/310
# which was backported to oz in
# https://src.fedoraproject.org/rpms/oz/c/4e5dbe2
# Might only be needed in imagefactory-plugins, but let's have it
# here just to be safe
Patch4: 0001-TinMan.py-adjust-to-oz-generate_diskimage-size-unit-.patch
# https://github.com/redhat-imaging/imagefactory/pull/459
# Python 3.12 support and CVE-2022-31799 fix for bundled bottle
Patch5: 0001-bottle-fix-for-Python-3.12-backport-CVE-2022-31799-f.patch
Patch6: 0002-Python-3.12-adjust-for-removal-of-SafeConfigParser.patch

BuildArch: noarch

BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildRequires: systemd-units

Requires: python3-pycurl
Requires: python3-libguestfs
Requires: python3-zope-interface
Requires: python3-libxml2
Requires: python3-httplib2
Requires: python3-cherrypy
Requires: python3-oauth2
Requires: python3-libs
# uses distutils at runtime, was removed from core Python in 3.12
Requires: python3-setuptools
Requires: oz

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# Has a vendored copy of bottle.py as imgfac/rest/bottle.py
Provides: bundled(python-bottle)

# TODO: Any changes to the _internal_ API must increment this version or, in
#       the case of backwards compatible changes, add a new version (RPM
#       allows multiple version "=" lines for the same package or
#       pseudo-package name)
Provides: imagefactory-plugin-api = 1.0

%description
imagefactory allows the creation of system images for multiple virtualization
and cloud providers from a single template definition. See
https://github.com/redhat-imaging/imagefactory for more information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n imagefactory-imagefactory-%{version}-1

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

%post
%systemd_post imagefactoryd.service

%preun
%systemd_preun imagefactoryd.service

%postun
%systemd_postun imagefactoryd.service

%files
%license COPYING
%{_unitdir}/imagefactoryd.service
%config(noreplace) %{_sysconfdir}/imagefactory/imagefactory.conf
%config(noreplace) %{_sysconfdir}/sysconfig/imagefactoryd
%config(noreplace) %{_sysconfdir}/logrotate.d/imagefactoryd
%dir %attr(0755, root, root) %{_sysconfdir}/pki/imagefactory/
%dir %attr(0755, root, root) %{_sysconfdir}/imagefactory/jeos_images/
%dir %attr(0755, root, root) %{_sysconfdir}/imagefactory/plugins.d/
%dir %attr(0755, root, root) %{_localstatedir}/lib/imagefactory/images
%config %{_sysconfdir}/pki/imagefactory/cert-ec2.pem
%{python3_sitelib}/imgfac/*.py*
%{python3_sitelib}/imgfac/__pycache__/*.py*
%{python3_sitelib}/imgfac/rest
%{python3_sitelib}/imagefactory-*.egg-info
%{_bindir}/imagefactory
%{_bindir}/imagefactoryd

%changelog
%autochangelog
