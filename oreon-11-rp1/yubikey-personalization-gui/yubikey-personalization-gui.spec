%global source0_hash 680b8ba8251c828847ffddd520165ac14927c2c6ee4ae39cfa9022ad7dd9dece

Name:           yubikey-personalization-gui
Version:        3.1.25
Release:        19%{?dist}
Summary:        GUI for Yubikey personalization

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://opensource.yubico.com/yubikey-personalization-gui/
Source0:        http://opensource.yubico.com/yubikey-personalization-gui/releases/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  libyubikey-devel >= 1.11
BuildRequires:  ykpers-devel >= 1.14.1
BuildRequires:  desktop-file-utils
BuildRequires:  qt-devel

%description
Yubico's YubiKey can be re-programmed with a new AES key. This is a graphical
tool that makes this an easy task.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{qmake_qt4} "CONFIG+=fedora"
make %{?_smp_mflags}

%install
install -D -p -m 0755 build/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 resources/lin/%{name}.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1

mkdir -p %{buildroot}/%{_datadir}/pixmaps
install -p -m 0644 resources/lin/%{name}.xpm %{buildroot}/%{_datadir}/pixmaps/
install -p -m 0644 resources/lin/%{name}.png %{buildroot}/%{_datadir}/pixmaps/

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    resources/lin/%{name}.desktop

%files
%doc NEWS README COPYING ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
