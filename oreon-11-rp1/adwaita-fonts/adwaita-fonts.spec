%global source0_hash 4c927fbfeec1c503801ba510c2c94e0054c82c522cf7ba0d3be5d4d41fcf5c86

%global tarball_version %%(echo %{version} | tr '~' '.')

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  fonts-rpm-macros

Version: 50.0
Release: %autorelease
License: OFL-1.1
URL:     https://gitlab.gnome.org/GNOME/adwaita-fonts.git

%global foundry         adwaita-fonts
%global fontdocs        README.md

%global common_description  %{expand:
Adwaita Fonts contains Adwaita Sans, a variation of Inter,
and Adwaita Mono, Iosevka customized to match Inter.
}

%global fontfamily1     adwaita-sans-fonts
%global fontsummary1    Adwaita Sans font family
%global fonts1          sans/*.ttf
%global fontlicenses1   LICENSE
%global fontconfs1      %{SOURCE1}
%global fontdescription1   %{expand:
%{common_description}
Adwaita Sans is a variation of the Inter font family.
}

%global fontfamily2     adwaita-mono-fonts
%global fontsummary2    Adwaita Mono font family
%global fonts2          mono/*.ttf
%global fontlicenses2   LICENSE
%global fontconfs2      %{SOURCE2}
%global fontdescription2   %{expand:
%{common_description}
Adwaita Mono is a customized version of the Iosevka font, designed to match Inter.
}

Source0:    https://download.gnome.org/sources/adwaita-fonts/50/adwaita-fonts-%{tarball_version}.tar.xz
Source1:    59-adwaita-sans-fonts.conf
Source2:    59-adwaita-mono-fonts.conf

Name:       adwaita-fonts
Summary:    Adwaita fonts
%description
%wordwrap -v common_description

%fontpkg -a
%fontmetapkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{tarball_version}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
