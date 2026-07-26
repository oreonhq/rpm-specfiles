%global source0_hash 2de22444da921fda7511680d569c9a936ec1147bf0124ac644cd95f58d5774f8

# Some Openstack supporting packages from EPEL have been removed due to updated
# deps that override RHEL and, thus, violate EPEL rules.  We would like to 
# eventually support these features as part of an EL6 and EL7 set of factory
# plugin packages in RDO.  Until this is sorted out we must disable things when
# building on RHEL.
# TODO: If we end up building as part of RDO either remove this for RDO
# SPEC builds or find a way to detect an RDO build and automagically negate this
# UPDATE: F24 dropped the supporting modules we currently use
# TODO: Refresh/refactor OpenStack support to use newer module and then update below
%if 0%{?fedora} >= 24 || 0%{?rhel} >= 3
%define include_openstack 0
%else
%define include_openstack 1
%endif

# For now, do not build this sub RPM - It has bitrotted and needs to be revisited
%define include_nova_image_builder 0

%global auto_register_macro_post() # create it if it doesn't already exist as a link \
# If it is an existing file other than a link, do nothing \
[ -L %{_sysconfdir}/imagefactory/plugins.d/%1.info ] || \
[ -e %{_sysconfdir}/imagefactory/plugins.d/%1.info ] || \
ln -s %{python3_sitelib}/imagefactory_plugins/%1/%1.info %{_sysconfdir}/imagefactory/plugins.d/%1.info \
exit 0 

%global auto_register_macro_postun() if [ "\$1" = "0" ]; then \
  # clean up the link if it exists - if it doesn't or if this is a regular file, do nothing \
  [ -L %{_sysconfdir}/imagefactory/plugins.d/%1.info ] && rm -f  %{_sysconfdir}/imagefactory/plugins.d/%1.info \
fi \
exit 0

Name: imagefactory-plugins
Version: 1.1.16
Release: 20%{?dist}
Summary: Default plugins for the Image Factory system image generation tool
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/redhat-imaging/imagefactory

Source0: https://github.com/redhat-imaging/imagefactory/archive/imagefactory-%{version}-1.tar.gz
Patch0: imagefactory-1.1.14-utf8-config-id.patch
Patch1: container-github-pr434.patch
Patch2: fix-armv7l.patch
# https://github.com/redhat-imaging/imagefactory/pull/455
Patch3: imagefactory-Docker.py-Pass-the-use_ino-option-to-fix-hardlnks.patch
# https://github.com/redhat-imaging/imagefactory/pull/458
# this goes along with https://github.com/clalancette/oz/pull/310
# which was backported to oz in
# https://src.fedoraproject.org/rpms/oz/c/4e5dbe2
Patch4: 0001-TinMan.py-adjust-to-oz-generate_diskimage-size-unit-.patch
# https://github.com/redhat-imaging/imagefactory/pull/459
# Python 3.12 support
Patch5: 0002-Python-3.12-adjust-for-removal-of-SafeConfigParser.patch

BuildArch: noarch
BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-devel
Requires: imagefactory

# Obsolete the old EC2 plugins as they need python2 based euca2ools thats not in Fedora anymore.
Obsoletes: imagefactory-plugins-EC2 < 1.1.15-3
Obsoletes: imagefactory-plugins-EC2-jeos-images < 1.1.15-3

%description
This is a placeholder top level package for a collection of plugins for the
Image Factory cloud system image generation tool.

imagefactory allows the creation of system images for multiple virtualization
and cloud providers from a single template definition. See
https://github.com/redhat-imaging/imagefactory for more information.

%package ovfcommon
Summary: common utilities to manipulate ovf-related objects
Requires: oz >= 0.7.0
Requires: imagefactory-plugins

%description ovfcommon
This pseudo-plugin is used to provide common OVF functionality to other
plugins.

%package OVA
Summary: Cloud plugin for generating OVA archives
Requires: oz >= 0.7.0
Requires: imagefactory-plugins
Requires: imagefactory-plugins-ovfcommon
Requires: imagefactory-plugin-api = 1.0

%description OVA
This Cloud plugin allows users to specify a Base Image to generate an OVA
archive from.

%package IndirectionCloud
Summary: Cloud plugin for allowing images to modify other images
Requires: oz >= 0.12.0
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description IndirectionCloud
This Cloud plugin allows users to specify a Base Image to use to manipulate
another Base Image to generate a Target Image.

It was originally created to produce Live CDs and other live media using an
arbitrary  host OS and package selection for the actual media creation tools.

%package TinMan
Summary: OS plugin for Fedora
Requires: oz >= 0.12.0
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description TinMan
An OS plugin to support Fedora OSes

%if 0%{include_openstack}
%package OpenStack
Summary: Cloud plugin for OpenStack running on KVM
Requires: python3-glanceclient
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description OpenStack
A Cloud plugin to support OpenStack running on top of KVM.

%package Rackspace
Summary: Cloud plugin for Rackspace
Requires: python-novaclient
Requires: python-pyrax
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description Rackspace
A Cloud plugin to support Rackspace

%package Rackspace-JEOS-images
Summary: JEOS images for various OSes to support Rackspace snapshot builds
Requires: imagefactory-plugins-Rackspace

%description Rackspace-JEOS-images
These configuration files point to existing JEOS Image ID's on Rackspace that
can be used to do "snapshot" style builds.
%endif

%if 0%{include_nova_image_builder}
%package Nova
Summary: OS plugin that allows imagefactory to use Nova instances to build base images.
Requires: python3-novaclient
Requires: oz >= 0.12.0
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description Nova
An alternative to the TinMan plugin for creating base images using an OpenStack cloud.
%endif

%if 0%{?build_mock}
%package MockOS
Summary: Mock OS plugin
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description MockOS
This plugin mimcs some of the behaviour of the RPM based OS plugins without
actually doing a build.

For testing use only.

%package MockCloud
Summary: Mock Cloud plugin
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description MockCloud
This plugin mimcs some of the behaviour of a real cloud plugin without needing
any real external infra.

For testing use only.

%endif

%package RHEVM
Summary: RHEVM Cloud plugin
Requires: imagefactory-plugins
Requires: imagefactory-plugins-ovfcommon
#Make optional for now to allow core coversion features to work
#Requires: ovirt-engine-sdk >= 3.1.0
Requires: qemu-img
Requires: imagefactory-plugin-api = 1.0

%description RHEVM
A plugin for RHEVM "clouds"

%package vSphere
Summary: vSphere Cloud plugin
Requires: imagefactory-plugins
#This has been made conditional in the plugin - will need to be replaced
#Requires: python-psphere
Requires: imagefactory-plugin-api = 1.0
Requires: qemu-img
Requires: python3-pyyaml

%description vSphere
A plugin for vSphere "clouds"

%package Docker
Summary: Cloud plugin for Docker
Requires: tar

%description Docker
A Cloud plugin to support Docker

%package HyperV
Summary: Cloud plugin for HyperV
Requires: qemu-img

%description HyperV
A Cloud plugin to support HyperV

%package GCE
Summary: Cloud plugin for GCE
Requires: qemu-img
Requires: tar

%description GCE
A Cloud plugin to support the Google Compute Engine

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n imagefactory-imagefactory-%{version}-1
mv imagefactory_plugins ../
rm -rf *
mv ../imagefactory_plugins/* .
rmdir ../imagefactory_plugins/
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p2
%patch -P4 -p2
%patch -P5 -p2

%build
%py3_build

%install
%py3_install

# TODO: Cleaner negative conditional
%if 0%{?build_mock}
%else
rm -rf %{buildroot}%{python3_sitelib}/imagefactory_plugins/MockOS
rm -rf %{buildroot}%{python3_sitelib}/imagefactory_plugins/MockCloud
%endif

%if 0%{include_openstack}
%else
rm -rf  %{buildroot}%{python3_sitelib}/imagefactory_plugins/OpenStack
rm -rf  %{buildroot}%{python3_sitelib}/imagefactory_plugins/Rackspace
rm -f  %{buildroot}%{_sysconfdir}/imagefactory/jeos_images/rackspace_fedora_jeos.conf
rm -f  %{buildroot}%{_sysconfdir}/imagefactory/jeos_images/rackspace_rhel_jeos.conf
%endif

%if 0%{include_nova_image_builder}
%else
rm -rf  %{buildroot}%{python3_sitelib}/imagefactory_plugins/Nova
%endif

# delete old EC2 and EC2-json-images plugins
rm -rf %{buildroot}%{_sysconfdir}/imagefactory/jeos_images
rm -rf %{buildroot}%{_bindir}/create-ec2-factory-credentials
rm -rf %{buildroot}%{python3_sitelib}/imagefactory_plugins/EC2

%post OVA
%auto_register_macro_post OVA
%postun OVA
%auto_register_macro_postun OVA

%post IndirectionCloud
%auto_register_macro_post IndirectionCloud
%postun IndirectionCloud
%auto_register_macro_postun IndirectionCloud

%post TinMan
%auto_register_macro_post TinMan
%postun TinMan
%auto_register_macro_postun TinMan

%if 0%{include_openstack}
%post OpenStack
%auto_register_macro_post OpenStack
%postun OpenStack
%auto_register_macro_postun OpenStack

%post Rackspace
%auto_register_macro_post Rackspace
%postun Rackspace
%auto_register_macro_postun Rackspace
%endif

%if 0%{include_nova_image_builder}
%post Nova
%auto_register_macro_post Nova
%postun Nova
%auto_register_macro_postrun Nova
%endif

%post RHEVM
%auto_register_macro_post RHEVM
%postun RHEVM
%auto_register_macro_postun RHEVM

%if 0%{?build_mock}
%post MockOS
%auto_register_macro_post MockOS
%postun MockOS
%auto_register_macro_postun MockOS

%post MockCloud
%auto_register_macro_post MockCloud
%postun MockCloud
%auto_register_macro_postun MockCloud
%endif

%post vSphere
%auto_register_macro_post vSphere
%postun vSphere
%auto_register_macro_postun vSphere

%post Docker
%auto_register_macro_post Docker
%postun Docker
%auto_register_macro_postun Docker

%post HyperV
%auto_register_macro_post HyperV
%postun HyperV
%auto_register_macro_postun HyperV

%post GCE
%auto_register_macro_post GCE
%postun GCE
%auto_register_macro_postun GCE

%files
%license COPYING
%dir %{python3_sitelib}/imagefactory_plugins
%{python3_sitelib}/imagefactory_plugins/__init__.py*
%{python3_sitelib}/imagefactory_plugins/__pycache__/*.py*
%{python3_sitelib}/imagefactory_plugins*.egg-info

%files ovfcommon
%dir %{python3_sitelib}/imagefactory_plugins/ovfcommon
%{python3_sitelib}/imagefactory_plugins/ovfcommon/*

%files OVA
%dir %{python3_sitelib}/imagefactory_plugins/OVA
%{python3_sitelib}/imagefactory_plugins/OVA/*

%files IndirectionCloud
%dir %{python3_sitelib}/imagefactory_plugins/IndirectionCloud
%{python3_sitelib}/imagefactory_plugins/IndirectionCloud/*

%files TinMan
%dir %{python3_sitelib}/imagefactory_plugins/TinMan
%{python3_sitelib}/imagefactory_plugins/TinMan/*

%if 0%{include_openstack}
%files OpenStack
%dir %{python3_sitelib}/imagefactory_plugins/OpenStack
%{python3_sitelib}/imagefactory_plugins/OpenStack/*

%files Rackspace
%dir %{python3_sitelib}/imagefactory_plugins/Rackspace
%{python3_sitelib}/imagefactory_plugins/Rackspace/*

%files Rackspace-JEOS-images
%{_sysconfdir}/imagefactory/jeos_images/rackspace_fedora_jeos.conf
%{_sysconfdir}/imagefactory/jeos_images/rackspace_rhel_jeos.conf
%endif

%if 0%{include_nova_image_builder}
%files Nova
%dir %{python3_sitelib}/imagefactory_plugins/Nova
%{python3_sitelib}/imagefactory_plugins/Nova/*
%endif

%if 0%{?build_mock}
%files MockOS
%dir %{python3_sitelib}/imagefactory_plugins/MockOS
%{python3_sitelib}/imagefactory_plugins/MockOS/*

%files MockCloud
%dir %{python3_sitelib}/imagefactory_plugins/MockCloud
%{python3_sitelib}/imagefactory_plugins/MockCloud/*
%endif

%files RHEVM
%dir %{python3_sitelib}/imagefactory_plugins/RHEVM
%{python3_sitelib}/imagefactory_plugins/RHEVM/*

%files vSphere
%dir %{python3_sitelib}/imagefactory_plugins/vSphere
%{python3_sitelib}/imagefactory_plugins/vSphere/*

%files Docker
%dir %{python3_sitelib}/imagefactory_plugins/Docker
%{python3_sitelib}/imagefactory_plugins/Docker/*

%files HyperV
%dir %{python3_sitelib}/imagefactory_plugins/HyperV
%{python3_sitelib}/imagefactory_plugins/HyperV/*

%files GCE
%dir %{python3_sitelib}/imagefactory_plugins/GCE
%{python3_sitelib}/imagefactory_plugins/GCE/*

%changelog
%autochangelog
