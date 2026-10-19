%global source0_hash d36b8a5b89bff0d8144efb57cbd315107502588818a2522cf32a2075c837de8c
ExcludeArch: %{ix86}
Name:           goverlay
Version:        1.9.2
Release:        1%{?dist}
Epoch:          1
Summary:        Graphical interface to configure MangoHud, vkBasalt, and OptiScaler
ExclusiveArch:  %{fpc_arches}
License:        GPL-3.0-or-later
URL:            https://github.com/benjamimgois/goverlay
Source0:        https://github.com/benjamimgois/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          goverlay-enable-debuginfo-generation.patch
Requires:       hicolor-icon-theme
Requires:       mangohud%{?_isa}
Requires:       mesa-libGLU
Requires:       qt6pas%{?_isa}
Recommends:     git%{?_isa}
Recommends:     mesa-demos%{?_isa}
Recommends:     vkBasalt%{?_isa}
Recommends:     vulkan-tools%{?_isa}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fpc-srpm-macros
BuildRequires:  lazarus
BuildRequires:  lazarus-lcl-qt6
BuildRequires:  libappstream-glib
BuildRequires:  libglvnd-devel
BuildRequires:  make
# /oreon:deps
%description
Goverlay helps Linux gamers get the most out of their system by offering an easy
graphical interface to configure MangoHud, vkBasalt, and OptiScaler. Whether you
want performance monitoring, visual enhancements, or smarter upscaling, Goverlay
makes everything accessible in just a few clicks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install prefix=%{_prefix}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
