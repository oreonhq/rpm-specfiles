%global source0_hash 0e2d6bb9c738d7016bb8af6780bef74dee263a02963e9c01a6b8331e7cafdf8d
%if 0%{?epel}
%bcond_with growpart
%else
%bcond_without growpart
%endif
Summary:        Cloud image management utilities
Name:		cloud-utils
Version:	0.34
Release:        1%{?dist}
License:	GPL-3.0-only
URL:		https://github.com/canonical/%{name}
Source0:        https://github.com/canonical/cloud-utils/archive/refs/tags/0.34.tar.gz#/cloud-utils-0.33.tar.gz
BuildArch:	noarch
Requires:	%{name}-growpart
Requires:	%{name}-cloud-localds
Requires:	%{name}-write-mime-multipart
Requires:	%{name}-ec2metadata
Requires:	%{name}-resize-part-image
Requires:	%{name}-mount-image-callback
Requires:	%{name}-vcs-run
# oreon:deps

# /oreon:deps
%description
This package provides a useful set of utilities for managing cloud images.

The tasks associated with image bundling are often tedious and repetitive. The
cloud-utils package provides several scripts that wrap the complicated tasks
with a much simpler interface.

%if %{with growpart}
%package growpart
Summary:	A script for growing a partition
Requires:	gawk
Requires:	util-linux
Recommends:	lvm2
%description growpart
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.
%endif

%package cloud-localds
Summary:	A script for creating a nocloud configuration disk for cloud-init
Recommends:	tar
Recommends:	dosfstools
Recommends:	mtools
Recommends:	genisoimage
Recommends:	qemu-img
%description cloud-localds
This package provides the cloud-localds script, which creates a disk-image
with user-data and/or meta-data for cloud-init.

%package write-mime-multipart
Summary:	A utilty for creating mime-multipart files
%description write-mime-multipart
This package provides the write-mime-multipart script, which creates
mime multipart files that can be consumed by cloud-init as user-data.

%package ec2metadata
Summary:	A script to query and display EC2 AMI instance metadata
%description ec2metadata
This package provides the ec2metadata script, which can be used to query and
display EC2 instance metadata rekated to an AMI instance.

%package resize-part-image
Summary:	A script for resizing cloud images
Requires:	file
Requires:	gzip
Requires:	e2fsprogs
Requires:	gawk
Requires:	tar
%description resize-part-image
This package provides the resize-part-image script, which can be used to
resize a partition image and the contained filesystem to a new size.

%package mount-image-callback
Summary:	A script to run commands over cloud image contents
Requires:	gawk
Requires:	util-linux
Recommends:	qemu-img
%description mount-image-callback
This package provides the mount-image-callback script, which mounts a cloud
image to a temporary mountpoint and runs a specified command on the contents.

%package vcs-run
Summary:	Script to run commands over a VCS repository contents
Recommends:	breezy
Recommends:	git-core
Recommends:	mercurial
Recommends:	wget
%description vcs-run
This package provides the vcs-run script, which fetches a code repository
into a temporary directory and runs a user-specified command in it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -pm 0755 bin/* %{buildroot}%{_bindir}/
install -pm 0644 man/* %{buildroot}%{_mandir}/man1/
rm -f %{buildroot}%{_bindir}/*ubuntu*
rm -f %{buildroot}%{_mandir}/man1/cloud-run-instances.*
rm -f %{buildroot}%{_bindir}/cloud-publish-*
rm -f %{buildroot}%{_mandir}/man1/cloud-publish-*
%if %{without growpart}
rm -f %{buildroot}%{_bindir}/growpart
rm -f %{buildroot}%{_mandir}/man1/growpart.*
%oreon_autofiles cloud-utils-growpart usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cloud-utils-cloud-localds usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cloud-utils-write-mime-multipart usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cloud-utils-ec2metadata usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cloud-utils-resize-part-image usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cloud-utils-mount-image-callback usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cloud-utils-vcs-run usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n cloud-utils-growpart -f %{oreon_filedir}/cloud-utils-growpart.list
%files -n cloud-utils-cloud-localds -f %{oreon_filedir}/cloud-utils-cloud-localds.list
%files -n cloud-utils-write-mime-multipart -f %{oreon_filedir}/cloud-utils-write-mime-multipart.list
%files -n cloud-utils-ec2metadata -f %{oreon_filedir}/cloud-utils-ec2metadata.list
%files -n cloud-utils-resize-part-image -f %{oreon_filedir}/cloud-utils-resize-part-image.list
%files -n cloud-utils-mount-image-callback -f %{oreon_filedir}/cloud-utils-mount-image-callback.list
%files -n cloud-utils-vcs-run -f %{oreon_filedir}/cloud-utils-vcs-run.list

%changelog

%autochangelog
