%global source0_hash a24edd604522b9a06a320a3c49f6f544bd88d2a6e40012ece3527fd53473aa8b
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
Name:       scl-utils
Epoch:      1
Version:    2.0.3
Release:        1%{?dist}
Summary:        Utilities for alternative packaging
License:    GPL-2.0-or-later
URL:        https://github.com/sclorg/scl-utils
Source0:        https://github.com/sclorg/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    macros.scl-filesystem
Requires:   %{_bindir}/modulecmd
Patch1:     0003-Scl-utils-layout-patch-from-fedora-famillecollet.com.patch
Patch2:     BZ-2056462-do-not-error-out-on-SIGINT.patch
Patch3:     BZ-2091000-remove-tmp-file.patch
Patch4:     brp-python-hardlink.patch
Patch5:     rpm-bare-words.patch
Patch6:     0001-add-missing-include.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  environment-modules
BuildRequires:  gcc
BuildRequires:  libcmocka
BuildRequires:  libcmocka-devel
BuildRequires:  make
BuildRequires:  rpm-devel
# /oreon:deps
%description
Run-time utility for alternative packaging.

%package build
Summary:    RPM build macros for alternative packaging
Requires:   iso-codes
Requires:   redhat-rpm-config
%description build
Essential RPM build macros for alternative packaging.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
sed -e '/CMAKE_MINIMUM_REQUIRED/s/2.6/3.5/' -i CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
if [ %{macrosdir} != %{_sysconfdir}/rpm ]; then
    mkdir -p %{buildroot}%{macrosdir}
    mv %{buildroot}%{_sysconfdir}/rpm/macros.scl %{buildroot}%{macrosdir}
    rmdir %{buildroot}%{_sysconfdir}/rpm
fi
cat %SOURCE1 >> %{buildroot}%{macrosdir}/macros.scl
mkdir -p %{buildroot}%{_sysconfdir}/scl
cd %{buildroot}%{_sysconfdir}/scl
mkdir modulefiles
mkdir prefixes
ln -s prefixes conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n scl-utils-build -f %{oreon_filedir}/scl-utils-build.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.3-8
- Prepare for Oreon 11 (RP1)
