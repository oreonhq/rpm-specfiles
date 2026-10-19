%global source0_hash 7099fcf6e94b6a6a8e57f8a3d434e7a66dbe476737f0f02f7bb3349586aa3b85
%global debug_package %{nil}
%ifarch aarch64
%bcond chainloading 1
%else
%bcond chainloading 0
%endif
%global fatfs_commit 87fc1ed5074a32b4e0344fcdde77359ef9e75432
Name:           m1n1
Version:        1.6.1
Release:        1%{?dist}
Summary:        Bootloader and experimentation playground for Apple Silicon
License:        MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later)
URL:            https://github.com/AsahiLinux/m1n1
Source0:        https://github.com/AsahiLinux/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          m1n1-rust-deps.patch
Patch:          rust-fatfs-fix-build-log.patch
%ifarch aarch64
%else
%endif
%global buildflags RELEASE=1
%if %{with chainloading}
%endif
Provides:       bundled(arm-trusted-firmware)
Provides:       bundled(dwc3)
Provides:       bundled(dlmalloc)
Provides:       bundled(PDCLib)
Provides:       bundled(libfdt)
Provides:       bundled(minilzlib)
Provides:       bundled(tinf)
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  adobe-source-code-pro-fonts
BuildRequires:  coreutils
BuildRequires:  fontconfig
BuildRequires:  gcc-aarch64-linux-gnu
BuildRequires:  make
BuildRequires:  system-logos
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%if %{with chainloading}
%package        stage1
Summary:        %{summary}
License:        MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0)
Provides:       bundled(crate(fatfs))= 0.4.0
%description    stage1

This package contains the stage1 build of m1n1 that is used by the Asahi Linux
Installer.
%endif

%package        tools
Summary:        Developer tools for m1n1
Requires:       %{name} = %{version}-%{release}
Requires:       python3
Requires:       python3dist(construct)
Requires:       python3dist(pyserial)
Requires:       systemd-udev
BuildArch:      noarch
%description    tools

This package contains various developer tools for m1n1.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N

# Use our logos
pushd data
ln -s %{_datadir}/pixmaps/bootloader/bootlogo_128.png fedora_128.png
ln -s %{_datadir}/pixmaps/bootloader/bootlogo_256.png fedora_256.png
popd

# Use our fonts
font="$(fc-match "Source Code Pro:bold" 'file' | cut -d= -f2)"
if [ ! -e "$font" ]; then
    echo "Failed to find font"
    exit 1
fi

pushd font
rm SourceCodePro-Bold.ttf font.bin font_retina.bin
./makefont.sh 8 16 12 "$font" font.bin
./makefont.sh 16 32 25 "$font" font_retina.bin
popd

%if %{with chainloading}
tar -xf %{SOURCE1} -C rust/vendor/rust-fatfs --strip-components 1
%autopatch -p1

%build

%if %{with chainloading}
%make_build %{buildflags} CHAINLOADING=1 LOGO=fedora
mv build build-stage1
pushd rust
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
popd
%endif
%make_build %{buildflags} LOGO=fedora
%install
install -Dpm0644 -t %{buildroot}%{_libdir}/%{name} \
  build/%{name}.{bin,macho} build/%{name}-asahi.bin
%if %{with chainloading}
install -Dpm0644 -t %{buildroot}%{_libdir}/%{name}-stage1 \
  build-stage1/%{name}.{bin,macho} build-stage1/%{name}-asahi.bin
%endif
install -Ddpm0755 %{buildroot}%{_libexecdir}/%{name}
cp -pr proxyclient tools %{buildroot}%{_libexecdir}/%{name}/
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} udev/80-m1n1.rules
install -Dpm0644 m1n1.conf.example %{buildroot}%{_sysconfdir}/m1n1.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n m1n1-tools -f %{oreon_filedir}/m1n1-tools.list

%changelog

%autochangelog
%endif
