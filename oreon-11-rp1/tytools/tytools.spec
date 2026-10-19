%global source0_hash 5d3017ea3a9a2d092b9407ec1858450c09be6268b05127a6c1dc7a0e87bfe48b
%global forgeurl https://github.com/Koromix/tytools
Name:           tytools
Version:        0.9.7
Release:        1%{?dist}
Summary:        Collection of tools to manage Teensy boards
License:        Unlicense
URL:            https://koromix.dev/tytools
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
TyTools is a collection of independent tools to manage Teensy microcontroller
boards.

%package -n     tycmd
Summary:        Command-line tool to manage Teensy boards
%description -n tycmd
tycmd is a command-line tool to manage Teensy boards.

%package -n     tycommander
Summary:        Upload, monitor and communicate with multiple Teensy boards
%description -n tycommander
TyCommander is a Qt GUI to upload, monitor and communicate with multiple Teensy
microcontroller boards.

%package -n     tyuploader
Summary:        Simple firmware / sketch uploader GUI for Teensy boards
%description -n tyuploader
TyUploader is a simple firmware / sketch uploader GUI for Teensy
microcontroller boards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles tycmd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles tycommander usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles tyuploader usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/tycommander.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/tyuploader.desktop
%files -f %{oreon_filedir}/main.list
%files -n tycmd -f %{oreon_filedir}/tycmd.list
%files -n tycommander -f %{oreon_filedir}/tycommander.list
%files -n tyuploader -f %{oreon_filedir}/tyuploader.list

%changelog

%autochangelog
