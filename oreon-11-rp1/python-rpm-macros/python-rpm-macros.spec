%global source303_hash 391c14688021ed40b50a22c99130648e3e000835c97bdbf104f0ed867f610fda
%global source301_hash 12849f6d7bb33858e6c00b4772aa6e518b5cd47ca104f2b88ddf81ed5ce024c5
%global source0_hash none
Name:           python-rpm-macros
Summary:        The common Python RPM macros
URL:            https://src.fedoraproject.org/rpms/python-rpm-macros/
Source101:      macros.python
Source102:      macros.python-srpm
Source104:      macros.python3
Source105:      macros.pybytecompile
Source106:      macros.python-wheel-sbom
Source201:      python.lua
%global compileall2_version 0.8.0
Source301:        https://github.com/fedora-python/compileall2/raw/v0.8.0/compileall2.py
Source302:      import_all_modules.py
%global pathfix_version 1.0.0
Source303:        https://github.com/fedora-python/pathfix/raw/v1.0.0/pathfix.py
Source304:      clamp_source_mtime.py
Source401:      brp-python-bytecompile
Source402:      brp-python-hardlink
Source403:      brp-fix-pyc-reproducibility
Source404:      brp-python-rpm-in-distinfo
License:        MIT AND PSF-2.0 AND GPL-2.0-or-later
%{lua:
if posix.stat(rpm.expand('%{SOURCE102}')) then
  rpm.load(rpm.expand('%{SOURCE102}'))
elseif posix.stat('macros.python-srpm') then
  -- something is parsing the spec without _sourcedir macro properly set
  rpm.load('macros.python-srpm')
end
}
Version:        %{__default_python3_version}
Release:        1%{?dist}
BuildArch:      noarch
Requires:       python-srpm-macros = %{version}-%{release}
%undefine __pythonname_provides
%undefine __pythonname_obsoletes
# oreon:deps

# /oreon:deps
%description
This package contains the unversioned Python RPM macros, that most
implementations should rely on.

You should not need to install this package manually as the various
python?-devel packages require it. So install a python-devel package instead.

%package -n python-srpm-macros
Summary:        RPM macros for building Python source packages
Requires:       redhat-rpm-config >= 190
Provides:       bundled(python3dist(compileall2)) = %{compileall2_version}
%description -n python-srpm-macros
RPM macros for building Python source packages.

%package -n python3-rpm-macros
Summary:        RPM macros for building Python 3 packages
Requires:       python-srpm-macros = %{version}-%{release}
Requires:       python-rpm-macros = %{version}-%{release}
%description -n python3-rpm-macros
RPM macros for building Python 3 packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -T
cp -a %{sources} .

# We want to have shebang in the script upstream but not here so
# the package with macros does not depend on Python.
sed -i '1s=^#!/usr/bin/env python3==' pathfix.py

%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644 macros.* %{buildroot}%{rpmmacrodir}/
mkdir -p %{buildroot}%{_rpmluadir}/fedora/srpm
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora/srpm python.lua
mkdir -p %{buildroot}%{_rpmconfigdir}/redhat
install -m 644 compileall2.py %{buildroot}%{_rpmconfigdir}/redhat/
install -m 644 clamp_source_mtime.py %{buildroot}%{_rpmconfigdir}/redhat/
install -m 644 import_all_modules.py %{buildroot}%{_rpmconfigdir}/redhat/
install -m 644 pathfix.py %{buildroot}%{_rpmconfigdir}/redhat/
install -m 755 brp-* %{buildroot}%{_rpmconfigdir}/redhat/
%define add_buildroot() %{lua:print((macros[macros[1]]:gsub(macros._rpmconfigdir, macros.buildroot .. macros._rpmconfigdir)))}
%global __brp_python_bytecompile %{add_buildroot __brp_python_bytecompile}
%global __brp_python_hardlink %{add_buildroot __brp_python_hardlink}
%global __brp_fix_pyc_reproducibility %{add_buildroot __brp_fix_pyc_reproducibility}
%global __brp_python_rpm_in_distinfo %{add_buildroot __brp_python_rpm_in_distinfo}
%oreon_autofiles python-srpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-rpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

grep -E '^#[^%%]*%%[^%%]' %{buildroot}%{rpmmacrodir}/macros.* && exit 1 || true
%files -f %{oreon_filedir}/main.list
%files -n python-srpm-macros -f %{oreon_filedir}/python-srpm-macros.list
%files -n python3-rpm-macros -f %{oreon_filedir}/python3-rpm-macros.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{__default_python3_version}-11
- Prepare for Oreon 11 (RP1)
