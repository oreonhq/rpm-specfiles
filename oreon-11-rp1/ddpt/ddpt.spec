%global source0_hash e340a529aeef6a107b0c24c64873da590f5284557faffdf57a0f9dc48807233d

Name:           ddpt
Version:        0.97
Release:        15%{?dist}
Summary:        Variant of the dd utility for SCSI/storage devices

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://sg.danny.cz/sg/ddpt.html
Source0:        http://sg.danny.cz/sg/p/%{name}-%{version}.tgz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  sg3_utils-devel
BuildRequires:  make

%description
The ddpt utility is a variant of the standard Unix command dd which copies
files. The ddpt utility specializes in files that are block devices. For block
devices that understand the SCSI command set, finer grain control over the
copy may be available via a SCSI pass-through interface. Note that recent
(S)ATA disks can often be driven by SCSI commands due to SCSI to ATA
translation (SAT) implemented in the kernel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING CREDITS ChangeLog README TODO doc/ddpt_examples.txt
%{_bindir}/%{name}*
%{_mandir}/man8/%{name}*.8*

%changelog
%autochangelog
