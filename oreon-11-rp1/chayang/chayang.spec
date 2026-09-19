%global source0_hash 61aa0e2955e8b5cf321ef14a5fd72f0e953da51a390d456e929b74fc5efcb74a

Name:           chayang
Version:        0.1.0

%global forgeurl https://git.sr.ht/~emersion/chayang
%global tag v%{version}
%forgemeta

Release:        %{autorelease}
Summary:        Gradually dim the screen on wlroots-based compositors

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  wayland-devel >= 1.14.91
BuildRequires:  wayland-protocols-devel >= 1.14

%description
Gradually dim the screen.
Can be used to implement a grace period before locking the session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
