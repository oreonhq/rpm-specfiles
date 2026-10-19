%global source4_hash b2247473a4ca18dff220ab95ea5c389edba1a23f184e2ac7d20454c2d8bb002d
%global source3_hash 2fbcd5f6daa300c14bd4e4867f09d5f1a5e36e437cc4dbb101c7931c11eadc08
%global source2_hash dafebf62b8737f341f6b7eca2d6d1153a50a6b1bfbfa4b8aaf0e62adc73e5017
%global source0_hash 898cdccca5c6627299c97251532023e123829bf4e764fbd644caab78c587a9d7
%global pypi_name asahi_firmware
%global debug_package %{nil}
%ifarch aarch64
%bcond installer_package 1
%else
%bcond installer_package 0
%endif
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif
%global liblzfse_majver 1
%global installer_libffi_version 3.5.2
%global installer_python_version 3.13.9
%global installer_python_asn1_version 2.5.0
%global installer_libffi_package libffi-%{installer_libffi_version}-macos.tar.gz
%global installer_python_package python-%{installer_python_version}-macos11.pkg
Name:           asahi-installer
Version:        0.9.2
Release:        1%{?dist}
Summary:        Asahi Linux installer
License:        MIT
URL:            https://github.com/AsahiLinux/asahi-installer
Source0:        https://github.com/AsahiLinux/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{installer_libffi_package}
Source2:        https://www.python.org/ftp/python/%{installer_python_version}/%{installer_python_package}
Source3:        https://www.python.org/ftp/python/%{installer_python_version}/%{installer_python_package}.asc
Source4:        https://keybase.io/nad/pgp_keys.asc?fingerprint=0d96df4d4110e5c43fbfb17f2d347ea6aa65421d#/key.asc
%if %{with installer_package}
%endif
ExcludeArch:    s390x
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-asahi-installer = %{version}-%{release}
# /oreon:deps
%description
Asahi Linux installer

%if %{with installer_package}
%package        package
Summary:        Asahi Linux Installer macOS package
License:        MIT AND (MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0)) AND Python
Provides:       bundled(libffi) = %{installer_libffi_version}
Provides:       bundled(python) = %{installer_python_version}
Provides:       bundled(python-asn1) = %{installer_python_asn1_version}
%description    package
macOS package for the Asahi Linux installer
%endif

%package -n     python3-%{pypi_name}
Summary:        Asahi Linux firmware tools
Requires:       liblzfse.so.%{liblzfse_majver}%{libsymbolsuffix}
Requires:       python3dist(asn1)
Requires:       tar
%description -n python3-%{pypi_name}
Asahi Linux firmware tools

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE2}'

# Set version
echo "%{version}" > version.tag

# Put the binary packages where the build script expects them
mkdir -p dl
ln -s %SOURCE1 %SOURCE2 dl/

%build

%if %{with installer_package}
M1N1_STAGE1="%{_libdir}/m1n1-stage1/m1n1.bin" \
LOGO="%{_datadir}/pixmaps/bootloader/fedora.icns" \
  ./build.sh
%endif
rm asahi_firmware/asn1.py
%pyproject_wheel
%install
%pyproject_install
%if %{with installer_package}
install -Dpm0644 -t %{buildroot}%{_libdir}/%{name}/releases releases/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%pyproject_check_import
%if %{with installer_package}
%files

%changelog

%autochangelog
%endif
