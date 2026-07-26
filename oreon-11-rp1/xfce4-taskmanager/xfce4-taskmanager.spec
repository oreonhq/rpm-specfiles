%global source0_hash 29bdc7840ab8b9025f6c0e456a83a31090d1c9fd9e26b359baa4a4010cfb0b90

%global majorversion 1.6

Name:           xfce4-taskmanager
Version:        1.6.0
Release:        %autorelease
Summary:        Taskmanager for the Xfce desktop environment

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/applications/%{name}
Source0:        http://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel
BuildRequires:  libXmu-devel
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  libwnck3-devel

%description
A simple taskmanager for the Xfce desktop environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

desktop-file-install \
    --delete-original \
    --add-category GTK \
    --add-category Monitor \
    --add-category X-Xfce \
    --remove-category Utility \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.taskmanager.*
%{_datadir}/icons/hicolor/scalable/actions/xc_crosshair-symbolic.svg

%changelog
%autochangelog
