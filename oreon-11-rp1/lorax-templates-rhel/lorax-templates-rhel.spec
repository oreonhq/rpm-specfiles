%global source0_hash none

Name:           lorax-templates-rhel
Version:        11.0
Release:        17%{?dist}
Summary:        RHEL build templates for lorax and livemedia-creator

License:        GPL-2.0-or-later
URL:            https://gitlab.com/redhat/centos-stream/rpms/lorax-templates-rhel/
BuildArch:      noarch

Source0:        https://gitlab.com/redhat/centos-stream/rpms/lorax-templates-rhel/-/archive/c11s/lorax-templates-rhel-c11s.tar.gz#/lorax-templates-rhel-%{version}.tar.gz

Requires:       lorax >= 34.9.1

Provides: lorax-templates = %{version}-%{release}

%define templatedir %{_datadir}/lorax/templates.d/80-rhel

%description
RHEL-specific Lorax templates for creating the boot.iso and live isos are
placed in %{templatedir}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n lorax-templates-rhel-c11s

%build

%install
install -d %{buildroot}%{templatedir}
cp -a 80-rhel/* %{buildroot}%{templatedir}/

%files
%dir %{templatedir}
%{templatedir}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11.0-17
- Import
