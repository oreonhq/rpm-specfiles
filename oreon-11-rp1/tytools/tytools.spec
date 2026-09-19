%global source0_hash 5d3017ea3a9a2d092b9407ec1858450c09be6268b05127a6c1dc7a0e87bfe48b

%global forgeurl https://github.com/Koromix/tytools

Name:           tytools
Version:        0.9.7
Release:        %autorelease
Summary:        Collection of tools to manage Teensy boards

License:        Unlicense
URL:            https://koromix.dev/tytools
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  systemd-devel

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

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

desktop-file-validate %{buildroot}/%{_datadir}/applications/tycommander.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/tyuploader.desktop

%files -n tycmd
%license LICENSE.txt
%doc README.md
%{_bindir}/tycmd

%files -n tycommander
%license LICENSE.txt
%doc README.md
%{_bindir}/tycommander
%{_datadir}/applications/tycommander.desktop

%files -n tyuploader
%license LICENSE.txt
%doc README.md
%{_bindir}/tyuploader
%{_datadir}/applications/tyuploader.desktop

%changelog
%autochangelog
