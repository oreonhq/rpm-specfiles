%global source0_hash none

Name:           lorax-templates-rhel
Version:        11.0
Release:        17%{?dist}
Summary:        RHEL build templates for lorax and livemedia-creator

License:        GPLv2+
%if 0%{?eln}
URL:            https://src.fedoraproject.org/rpms/lorax-templates-rhel/
%else
URL:            https://gitlab.com/redhat/centos-stream/rpms/lorax-templates-rhel/
%endif
BuildArch:      noarch

# This tarball is generated from the contents of this dist-git repository
# by running the command `make tar`.
# See README for full details of how to update this package
Source0:        lorax-templates-rhel-11.0-17.tar.gz

# Required for the template branding support
Requires:       lorax >= 34.9.1

Provides: lorax-templates = %{version}-%{release}

# Where are these supposed to end up?
%define templatedir %{_datadir}/lorax/templates.d/80-rhel

%description
RHEL-specific Lorax templates for creating the boot.iso and live isos are
placed in %{templatedir}

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup

%build
# nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{templatedir}
cp -a 80-rhel/* $RPM_BUILD_ROOT/%{templatedir}

%files
%dir %{templatedir}
%{templatedir}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11.0-17
- Import
